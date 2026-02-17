#!/usr/bin/env python3
"""
Python 학습 실행 도구
====================
챕터 파일이나 연습장을 실행하고, 출력 결과를 보기 좋게 표시합니다.

사용법:
    python run.py              → 연습장(playground.py) 실행
    python run.py play         → 연습장(playground.py) 실행
    python run.py watch        → 연습장 감시 모드 (저장하면 자동 실행!)
    python run.py watch 3      → ch03 감시 모드
    python run.py 1            → ch01 실행
    python run.py ch05         → ch05 실행
    python run.py list         → 챕터 목록 보기
    python run.py all          → 전체 챕터 실행
"""

import subprocess
import sys
import os
import time
import glob

# ─── 색상 코드 (터미널 출력용) ─────────────────────────────────────
class Color:
    HEADER  = "\033[95m"
    BLUE    = "\033[94m"
    CYAN    = "\033[96m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    RED     = "\033[91m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RESET   = "\033[0m"


# ─── 상수 ──────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARTS = [
    ("part1_basics",        "Part 1. 파이썬 기초"),
    ("part2_intermediate",  "Part 2. 파이썬 중급"),
    ("part3_data_science",  "Part 3. 데이터 사이언스"),
]
PLAYGROUND = os.path.join(BASE_DIR, "playground.py")


# ─── 유틸리티 함수 ─────────────────────────────────────────────────
def print_banner():
    """학습 도구 배너 출력"""
    banner = f"""
{Color.CYAN}{Color.BOLD}╔══════════════════════════════════════════════════╗
║          🐍 Python 학습 실행 도구               ║
╚══════════════════════════════════════════════════╝{Color.RESET}"""
    print(banner, flush=True)


def print_separator(char="─", length=52):
    print(f"{Color.DIM}{char * length}{Color.RESET}")


def find_all_chapters():
    """모든 챕터 파일을 찾아서 정렬된 리스트로 반환"""
    chapters = []
    for folder, part_name in PARTS:
        folder_path = os.path.join(BASE_DIR, folder)
        if not os.path.isdir(folder_path):
            continue
        files = sorted(glob.glob(os.path.join(folder_path, "ch*.py")))
        for f in files:
            chapters.append((f, part_name))
    return chapters


def extract_chapter_info(filepath):
    """파일에서 챕터 제목 추출"""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines[:5]:
            stripped = line.strip().strip('"').strip("'")
            if stripped.startswith("Chapter") or stripped.startswith("chapter"):
                return stripped
        # docstring의 두 번째 줄 시도
        if len(lines) >= 2:
            candidate = lines[1].strip().strip('"').strip("'")
            if candidate and not candidate.startswith("="):
                return candidate
    except Exception:
        pass
    return os.path.basename(filepath)


def resolve_target(arg):
    """사용자 입력을 파일 경로로 변환"""
    # 'play' 또는 'playground' → 연습장
    if arg.lower() in ("play", "playground", "p"):
        return PLAYGROUND

    # 숫자만 입력한 경우: 1 → ch01
    if arg.isdigit():
        ch_num = int(arg)
        pattern = f"ch{ch_num:02d}_*.py"
    # 'ch01' 등 입력한 경우
    elif arg.lower().startswith("ch"):
        pattern = f"{arg.lower()}*.py"
    else:
        # 직접 파일 경로
        if os.path.isfile(arg):
            return arg
        pattern = f"*{arg}*.py"

    # 모든 파트에서 검색
    for folder, _ in PARTS:
        folder_path = os.path.join(BASE_DIR, folder)
        matches = glob.glob(os.path.join(folder_path, pattern))
        if matches:
            return sorted(matches)[0]

    return None


def run_python_file(filepath):
    """Python 파일을 실행하고 결과를 표시"""
    filename = os.path.basename(filepath)
    rel_path = os.path.relpath(filepath, BASE_DIR)
    title = extract_chapter_info(filepath)

    print()
    print(f"{Color.BOLD}{Color.GREEN}▶ 실행: {rel_path}{Color.RESET}")
    if title != filename:
        print(f"  {Color.DIM}{title}{Color.RESET}")
    print_separator("━")
    print(flush=True)
    sys.stdout.flush()

    start_time = time.time()

    try:
        result = subprocess.run(
            [sys.executable, filepath],
            cwd=BASE_DIR,
            capture_output=False,
            text=True,
            timeout=30,
        )
        elapsed = time.time() - start_time

        print()
        print_separator("━")

        if result.returncode == 0:
            print(
                f"{Color.GREEN}✓ 완료{Color.RESET} "
                f"{Color.DIM}({elapsed:.2f}초){Color.RESET}"
            )
        else:
            print(
                f"{Color.RED}✗ 오류 발생 (exit code: {result.returncode}){Color.RESET} "
                f"{Color.DIM}({elapsed:.2f}초){Color.RESET}"
            )
        return result.returncode

    except subprocess.TimeoutExpired:
        elapsed = time.time() - start_time
        print()
        print_separator("━")
        print(
            f"{Color.YELLOW}⏱ 시간 초과 (30초){Color.RESET} "
            f"- input() 등 사용자 입력이 필요한 코드는 직접 실행하세요."
        )
        return 1

    except Exception as e:
        print()
        print_separator("━")
        print(f"{Color.RED}✗ 실행 실패: {e}{Color.RESET}")
        return 1


def list_chapters():
    """챕터 목록 출력"""
    print_banner()
    print()

    chapters = find_all_chapters()
    current_part = None

    for filepath, part_name in chapters:
        if part_name != current_part:
            current_part = part_name
            print(f"\n{Color.BOLD}{Color.BLUE}  {part_name}{Color.RESET}")
            print_separator("─")

        filename = os.path.basename(filepath)
        # ch01_hello.py → 01
        ch_num = filename[2:4]
        title = extract_chapter_info(filepath)
        if title == filename:
            title = filename.replace(".py", "").replace("_", " ")

        print(f"    {Color.CYAN}{ch_num}{Color.RESET}  {title}")

    print()
    print_separator("─")
    print(f"  {Color.DIM}실행: python run.py [번호]  |  연습장: python run.py play{Color.RESET}")
    print()


def watch_file(filepath):
    """파일 변경을 감시하고 저장될 때마다 자동 실행"""
    rel_path = os.path.relpath(filepath, BASE_DIR)

    print_banner()
    print(f"""
{Color.BOLD}{Color.YELLOW}👀 감시 모드 시작{Color.RESET}
{Color.DIM}   파일: {rel_path}
   파일을 저장(Cmd+S)하면 자동으로 실행됩니다.
   종료: Ctrl+C{Color.RESET}
""", flush=True)

    print_separator("─")
    print(f"{Color.DIM}  첫 실행 중...{Color.RESET}", flush=True)
    run_python_file(filepath)

    last_mtime = os.path.getmtime(filepath)
    run_count = 1

    try:
        while True:
            time.sleep(0.5)
            try:
                current_mtime = os.path.getmtime(filepath)
            except OSError:
                continue

            if current_mtime != last_mtime:
                last_mtime = current_mtime
                run_count += 1

                # 화면 구분을 위한 헤더
                print(f"\n\n{Color.CYAN}{Color.BOLD}", end="")
                print(f"{'=' * 52}")
                print(f"  💾 변경 감지! (#{run_count}) 다시 실행합니다...")
                print(f"{'=' * 52}{Color.RESET}", flush=True)

                run_python_file(filepath)

                print(f"\n{Color.DIM}  👀 저장을 기다리는 중... (Ctrl+C로 종료){Color.RESET}",
                      flush=True)

    except KeyboardInterrupt:
        print(f"\n\n{Color.YELLOW}👋 감시 모드를 종료합니다.{Color.RESET}")
        print(f"{Color.DIM}   총 {run_count}회 실행했습니다.{Color.RESET}\n")


def show_help():
    """도움말 출력"""
    print_banner()
    print(f"""
{Color.BOLD}사용법:{Color.RESET}
    python run.py              연습장(playground.py) 실행
    python run.py play         연습장(playground.py) 실행
    python run.py {Color.YELLOW}watch{Color.RESET}        연습장 감시 모드 {Color.YELLOW}← 저장하면 자동 실행!{Color.RESET}
    python run.py {Color.YELLOW}watch 3{Color.RESET}      ch03 파일 감시 모드
    python run.py {Color.CYAN}1{Color.RESET}            ch01 챕터 실행
    python run.py {Color.CYAN}ch05{Color.RESET}         ch05 챕터 실행
    python run.py list         전체 챕터 목록 보기
    python run.py all          모든 챕터 순서대로 실행
    python run.py help         이 도움말 보기

{Color.BOLD}팁:{Color.RESET}
    {Color.DIM}• 연습장(playground.py)에서 자유롭게 코드를 작성하고 실행해 보세요.
    • 'python run.py watch'로 감시 모드를 켜면 저장할 때마다 자동 실행됩니다!
    • Cursor에서 Cmd+Shift+B 로 현재 파일을 바로 실행할 수 있습니다.
    • 각 챕터 파일 하단의 연습 문제를 꼭 풀어 보세요!{Color.RESET}
""")


# ─── 메인 ──────────────────────────────────────────────────────────
def main():
    args = sys.argv[1:]

    # 인자 없이 실행 → 연습장 실행
    if not args:
        print_banner()
        if os.path.isfile(PLAYGROUND):
            run_python_file(PLAYGROUND)
        else:
            print(f"\n{Color.YELLOW}연습장 파일이 없습니다: playground.py{Color.RESET}")
            print(f"{Color.DIM}playground.py 파일을 생성해 주세요.{Color.RESET}\n")
        return

    cmd = args[0].lower()

    if cmd in ("help", "-h", "--help"):
        show_help()

    elif cmd in ("watch", "w"):
        # watch 뒤에 대상 지정 가능: watch 3 → ch03 감시
        if len(args) >= 2:
            target = resolve_target(args[1])
        else:
            target = PLAYGROUND

        if target and os.path.isfile(target):
            watch_file(target)
        else:
            label = args[1] if len(args) >= 2 else "playground.py"
            print(f"\n{Color.RED}✗ 감시할 파일을 찾을 수 없음: '{label}'{Color.RESET}")
            print(f"{Color.DIM}  'python run.py list'로 사용 가능한 챕터를 확인하세요.{Color.RESET}\n")

    elif cmd in ("list", "ls", "l"):
        list_chapters()

    elif cmd in ("all", "a"):
        print_banner()
        chapters = find_all_chapters()
        total = len(chapters)
        passed = 0
        failed = 0

        for i, (filepath, _) in enumerate(chapters, 1):
            print(f"\n{Color.DIM}[{i}/{total}]{Color.RESET}")
            code = run_python_file(filepath)
            if code == 0:
                passed += 1
            else:
                failed += 1

        print(f"\n\n{Color.BOLD}═══ 전체 결과 ═══{Color.RESET}")
        print(f"  {Color.GREEN}성공: {passed}{Color.RESET}  ", end="")
        print(f"  {Color.RED}실패: {failed}{Color.RESET}  ", end="")
        print(f"  합계: {total}")
        print()

    else:
        # 챕터 번호 또는 파일명으로 실행
        print_banner()
        target = resolve_target(args[0])
        if target and os.path.isfile(target):
            run_python_file(target)
        else:
            print(f"\n{Color.RED}✗ 찾을 수 없음: '{args[0]}'{Color.RESET}")
            print(f"{Color.DIM}  'python run.py list'로 사용 가능한 챕터를 확인하세요.{Color.RESET}\n")


if __name__ == "__main__":
    main()
