#!/usr/bin/env python3
"""
챕터 파일 파서: Python 학습 파일을 웹 앱용 JSON 데이터로 변환합니다.
"""
import json
import re
import os
import sys

PARTS = {
    "part1_basics": {"num": 1, "title": "파이썬 기초", "icon": "🌱"},
    "part2_intermediate": {"num": 2, "title": "파이썬 중급", "icon": "🌿"},
    "part3_data_science": {"num": 3, "title": "데이터 사이언스", "icon": "🔬"},
}

SEPARATOR = re.compile(r"^# ={40,}$")


def classify_line(line):
    stripped = line.strip()
    if stripped == "":
        return "empty"
    if stripped.startswith("#"):
        return "comment"
    return "code"


def strip_comment(line):
    s = line.strip()
    if s == "#":
        return ""
    if s.startswith("# "):
        return s[2:]
    if s.startswith("#"):
        return s[1:]
    return s


def parse_blocks(lines):
    """Parse lines into alternating text/code blocks."""
    blocks = []
    current_type = None
    current_lines = []
    pending_empty = 0
    in_docstring = False

    def flush():
        nonlocal current_type, current_lines, pending_empty
        if current_lines:
            content = "\n".join(current_lines).strip()
            if content:
                blocks.append({"type": current_type, "content": content})
        current_type = None
        current_lines = []
        pending_empty = 0

    for line in lines:
        stripped = line.strip()

        if '"""' in stripped or "'''" in stripped:
            delim = '"""' if '"""' in stripped else "'''"
            count = stripped.count(delim)
            if count == 1:
                in_docstring = not in_docstring
                if in_docstring:
                    flush()
                    current_type = "comment"
                    rest = stripped.split(delim, 1)[1]
                    if rest:
                        current_lines.append(rest)
                else:
                    rest = stripped.split(delim, 1)[0]
                    if rest:
                        current_lines.append(rest)
                    flush()
                continue
            elif count >= 2:
                inner = stripped.split(delim, 2)
                if len(inner) >= 2 and inner[1].strip():
                    flush()
                    blocks.append({"type": "comment", "content": inner[1].strip()})
                continue

        if in_docstring:
            current_lines.append(stripped)
            continue

        kind = classify_line(line)

        if kind == "empty":
            pending_empty += 1
            continue

        if kind == "comment":
            text = strip_comment(line)
            if current_type == "comment":
                for _ in range(pending_empty):
                    current_lines.append("")
                pending_empty = 0
                current_lines.append(text)
            else:
                flush()
                current_type = "comment"
                current_lines.append(text)
        elif kind == "code":
            if current_type == "code":
                for _ in range(pending_empty):
                    current_lines.append("")
                pending_empty = 0
                current_lines.append(line.rstrip())
            else:
                flush()
                current_type = "code"
                current_lines.append(line.rstrip())

    flush()

    result = []
    for b in blocks:
        btype = "text" if b["type"] == "comment" else "code"
        result.append({"type": btype, "content": b["content"]})
    return result


def extract_code(blocks):
    """Extract only code from blocks for the 'Try it' feature."""
    code_parts = []
    for b in blocks:
        if b["type"] == "code":
            code_parts.append(b["content"])
    return "\n\n".join(code_parts)


def parse_exercises(content):
    """Extract exercises from docstring content."""
    exercises = []
    pattern = re.compile(r"\[연습\s*(\d+)\]\s*(.+?)(?=\[연습|\Z)", re.DOTALL)
    for m in pattern.finditer(content):
        exercises.append({
            "number": int(m.group(1)),
            "description": m.group(2).strip(),
        })
    return exercises


def find_sections(lines):
    """Find section boundaries marked by # === separators."""
    sections = []
    i = 0
    while i < len(lines):
        if SEPARATOR.match(lines[i].strip()):
            if i + 2 < len(lines) and SEPARATOR.match(lines[i + 2].strip()):
                title = lines[i + 1].strip().lstrip("#").strip()
                sections.append({"start": i, "title_line": i + 1, "end_sep": i + 2, "title": title})
                i += 3
                continue
        i += 1
    return sections


def parse_chapter(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    lines = content.split("\n")

    filename = os.path.basename(filepath)
    ch_match = re.match(r"ch(\d+)_(.+)\.py", filename)
    if not ch_match:
        return None
    ch_num = int(ch_match.group(1))

    part_dir = os.path.basename(os.path.dirname(filepath))
    part_info = PARTS.get(part_dir, {"num": 0, "title": "", "icon": ""})

    doc_match = re.search(r'"""\s*\n(.+?)\n={3,}\n(.*?)\n"""', content, re.DOTALL)
    title = ""
    description = ""
    if doc_match:
        raw_title = doc_match.group(1).strip()
        title = re.sub(r"^Chapter\s+\d+:\s*", "", raw_title)
        description = doc_match.group(2).strip()

    section_markers = find_sections(lines)
    sections = []

    for idx, marker in enumerate(section_markers):
        content_start = marker["end_sep"] + 1
        content_end = section_markers[idx + 1]["start"] if idx + 1 < len(section_markers) else len(lines)
        section_lines = lines[content_start:content_end]

        sec_title = marker["title"]
        is_comparison = "JavaScript" in sec_title or "vs" in sec_title.lower()
        is_exercise = "연습" in sec_title

        if is_comparison:
            raw_text = "\n".join(section_lines).strip()
            comment_lines = []
            for ln in section_lines:
                s = ln.strip()
                if s.startswith("#"):
                    comment_lines.append(strip_comment(ln))
            sections.append({
                "title": sec_title,
                "type": "comparison",
                "blocks": [{"type": "text", "content": "\n".join(comment_lines).strip()}],
                "code": "",
            })
        elif is_exercise:
            full_text = "\n".join(section_lines)
            doc = re.search(r'"""(.*?)"""', full_text, re.DOTALL)
            exercises = []
            if doc:
                exercises = parse_exercises(doc.group(1))
            sections.append({
                "title": sec_title,
                "type": "exercise",
                "blocks": [],
                "exercises": exercises,
                "code": "",
            })
        else:
            blocks = parse_blocks(section_lines)
            code = extract_code(blocks)
            sections.append({
                "title": sec_title,
                "type": "content",
                "blocks": blocks,
                "code": code,
            })

    return {
        "id": f"ch{ch_num:02d}",
        "number": ch_num,
        "title": title,
        "description": description,
        "part": part_info["num"],
        "partTitle": part_info["title"],
        "partIcon": part_info["icon"],
        "sections": sections,
    }


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    chapters = []

    for part_dir in sorted(PARTS.keys()):
        part_path = os.path.join(base_dir, part_dir)
        if not os.path.isdir(part_path):
            continue
        for ch_file in sorted(os.listdir(part_path)):
            if ch_file.startswith("ch") and ch_file.endswith(".py"):
                filepath = os.path.join(part_path, ch_file)
                chapter = parse_chapter(filepath)
                if chapter:
                    chapters.append(chapter)
                    print(f"  ✓ {chapter['id']}: {chapter['title']} ({len(chapter['sections'])} sections)")

    output_dir = os.path.join(base_dir, "web", "js")
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "chapters-data.js")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated by scripts/build_chapters.py — DO NOT EDIT\n")
        f.write("const CHAPTERS_DATA = ")
        json.dump(chapters, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    print(f"\n✅ Generated {len(chapters)} chapters → {output_path}")


if __name__ == "__main__":
    main()
