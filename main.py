from datetime import datetime

import gifos
from zoneinfo import ZoneInfo

FONT_FILE_LOGO = "gifos/fonts/vtks-blocketo.regular.ttf"
# FONT_FILE_BITMAP = "./fonts/ter-u14n.pil"
FONT_FILE_BITMAP = "gifos/fonts/gohufont-uni-14.pil"
FONT_FILE_TRUETYPE = "gifos/fonts/IosevkaTermNerdFont-Bold.ttf"
FONT_FILE_MONA = "gifos/fonts/Inversionz.otf"


def main():
    t = gifos.Terminal(750, 500, 15, 15, FONT_FILE_BITMAP, 15)

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    year_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime("%Y")
    t.gen_text("GIF_OS Modular BIOS v1.0.11", 1)
    # t.gen_text(f"Copyright (C) {year_now}, \x1b[31mX0rzAvi Softwares Inc.\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile ReadMe Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("Krypton(tm) GIFCPU - 250Hz", 6)
    t.gen_text(
        "Press \x1b[94mDEL\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to cancel Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653, 7168):  # 64K Memory
        t.delete_row(7)
        if i < 30000:
            t.gen_text(
                f"Memory Test: {i}", 7, count=2, contin=True
            )  # slow down upto a point
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64KB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)  # buffer to be removed
    t.set_font(FONT_FILE_LOGO, 66)
    # t.toggle_show_cursor(True)
    os_logo_text = "GIF OS"
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    t.set_font(FONT_FILE_BITMAP, 15)
    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mGIF OS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    
    # block_lines = [
    # "\x1b[48;2;234;242;242m  \x1b[48;2;227;235;238m  \x1b[48;2;226;236;241m  \x1b[48;2;230;239;241m  \x1b[48;2;226;232;234m  \x1b[48;2;220;226;227m  \x1b[0m",
    # "\x1b[48;2;214;225;228m  \x1b[48;2;211;221;225m  \x1b[48;2;162;167;170m  \x1b[48;2;144;146;149m  \x1b[48;2;189;196;199m  \x1b[48;2;199;210;214m  \x1b[0m",
    # "\x1b[48;2;155;173;166m  \x1b[48;2;156;172;171m  \x1b[48;2;90;77;70m  \x1b[48;2;93;68;60m  \x1b[48;2;113;112;104m  \x1b[48;2;107;118;103m  \x1b[0m",
    # "\x1b[48;2;112;124;61m  \x1b[48;2;112;123;71m  \x1b[48;2;122;104;88m  \x1b[48;2;138;99;84m  \x1b[48;2;138;133;121m  \x1b[48;2;116;121;86m  \x1b[0m",
    # "\x1b[48;2;124;130;69m  \x1b[48;2;120;128;102m  \x1b[48;2;168;172;188m  \x1b[48;2;173;165;168m  \x1b[48;2;81;92;111m  \x1b[48;2;169;175;185m  \x1b[0m",
    # "\x1b[48;2;104;105;55m  \x1b[48;2;144;147;131m  \x1b[48;2;180;193;222m  \x1b[48;2;162;177;209m  \x1b[48;2;53;59;73m  \x1b[48;2;168;170;185m  \x1b[0m",
    # "\x1b[48;2;234;242;242m  \x1b[48;2;227;235;238m  \x1b[48;2;226;236;241m  \x1b[48;2;230;239;241m  \x1b[48;2;226;232;234m  \x1b[48;2;220;226;227m  \x1b[0m",
    # "\x1b[48;2;214;225;228m  \x1b[48;2;211;221;225m  \x1b[48;2;162;167;170m  \x1b[48;2;144;146;149m  \x1b[48;2;189;196;199m  \x1b[48;2;199;210;214m  \x1b[0m",
    # "\x1b[48;2;155;173;166m  \x1b[48;2;156;172;171m  \x1b[48;2;90;77;70m  \x1b[48;2;93;68;60m  \x1b[48;2;113;112;104m  \x1b[48;2;107;118;103m  \x1b[0m",
    # "\x1b[48;2;112;124;61m  \x1b[48;2;112;123;71m  \x1b[48;2;122;104;88m  \x1b[48;2;138;99;84m  \x1b[48;2;138;133;121m  \x1b[48;2;116;121;86m  \x1b[0m",
    # "\x1b[48;2;124;130;69m  \x1b[48;2;120;128;102m  \x1b[48;2;168;172;188m  \x1b[48;2;173;165;168m  \x1b[48;2;81;92;111m  \x1b[48;2;169;175;185m  \x1b[0m",
    # "\x1b[48;2;104;105;55m  \x1b[48;2;144;147;131m  \x1b[48;2;180;193;222m  \x1b[48;2;162;177;209m  \x1b[48;2;53;59;73m  \x1b[48;2;168;170;185m  \x1b[0m",
    # ]

    # # Create a "line" of 4 asterisks by repeating horizontally
    # final_password_rows = []
    # for row in block_lines:
    #     final_password_rows.append(row * 4)  # Repeat 4 times horizontally

    # Render each row starting from the current row
    t.gen_typing_text("hardik4tiwari", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.set_font(FONT_FILE_TRUETYPE, 12)
    with open("docs/assets/ascii-art.txt", "r") as art:
        lines = art.readlines()

    for i, line in enumerate(lines):
        t.gen_text(f"\x1b[90m{line.rstrip()}\x1b[0m", 5 + i, 25,contin=True)
    # start_row = 4
    # for i, line in enumerate(final_password_rows):
    #     t.gen_text(line, start_row + i)
    # t.gen_typing_text("*********", 4, contin=True)
    t.set_font(FONT_FILE_BITMAP,15)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Asia/Kolkata")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    print(prompt_col)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)  # simulate syntax highlighting
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)
    
    ignore_repos = []
    git_user_details = gifos.utils.fetch_github_stats("hardik4tiwari", ignore_repos)
    user_age = gifos.utils.calc_age(3, 12, 2004)
    t.clear_frame()
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    user_details_lines = f"""
    \x1b[30;101mhardik4tiwari@GitHub\x1b[0m
    --------------
    \x1b[96mOS:     \x1b[93mLinux, Windows 11, iOS\x1b[0m
    \x1b[96mHost:   \x1b[93mIndian Institute of Technology Kanpur \x1b[0m
    \x1b[96mKernel: \x1b[93mCivil Engineering \x1b[0m
    \x1b[96mUptime: \x1b[93m{user_age.years} years, {user_age.months} months, {user_age.days} days\x1b[0m
    \x1b[96mIDE:    \x1b[93mVSCode\x1b[0m
    
    \x1b[30;101mContact:\x1b[0m
    --------------
    \x1b[96mEmail:      \x1b[93mhardnotik@gmail.com\x1b[0m
    \x1b[96mLinkedIn:   \x1b[93mhardik4tiwari\x1b[0m
    
    \x1b[30;101mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mUser Rating: \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars Earned: \x1b[93m{git_user_details.total_stargazers}\x1b[0m
    \x1b[96mTotal Commits ({int(year_now) - 1}): \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs: \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR %: \x1b[93m{git_user_details.pull_requests_merge_percentage}\x1b[0m
    \x1b[96mTotal Contributions: \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
    \x1b[96mTop Languages: \x1b[93m{', '.join(top_languages[1:5])}\x1b[0m
    """
    t.gen_prompt(1)
    prompt_col = t.curr_col
    print(prompt_col)
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u hardik4tiwari", 1, contin=True)

    t.set_font(FONT_FILE_MONA, 16, 0)
    t.toggle_show_cursor(False)
    monaLines = r"""
    \x1b[49m     \x1b[90;100m}}\x1b[49m     \x1b[90;100m}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}\x1b[49m   \x1b[90;100m}}}}\x1b[0m
    \x1b[49m    \x1b[90;100m}}}}}\x1b[49m \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}}}}}}}}}}}}}\x1b[0m
    \x1b[49m   \x1b[90;100m}}\x1b[37;47m}}}}}}}\x1b[90;100m}}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}}\x1b[37;47m}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}\x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}\x1b[37;47m}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}}}\x1b[37;47m}}}}\x1b[90;100m}}}\x1b[37;47m}}}}}\x1b[90;100m}}}}\x1b[0m
    \x1b[49m  \x1b[90;100m}\x1b[37;47m}}}}}\x1b[90;100m}}\x1b[37;47m}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[49m \x1b[90;100m}}\x1b[37;47m}}}}}}}}}}}}\x1b[90;100m}}}\x1b[0m
    \x1b[90;100m}\x1b[49m  \x1b[90;100m}}\x1b[37;47m}}}}}}}}\x1b[90;100m}}}\x1b[49m  \x1b[90;100m}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m       \x1b[90;100m}}}}}}}}\x1b[0m
    \x1b[49m      \x1b[90;100m}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}}}}}}}}}}}\x1b[0m
    \x1b[49m     \x1b[90;100m}}\x1b[49m \x1b[90;100m}}}}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    \x1b[49m        \x1b[90;100m}}}}}}}\x1b[0m
    \x1b[49m         \x1b[90;100m}}}\x1b[49m \x1b[90;100m}}\x1b[0m
    """
    t.gen_text(monaLines, 10)

    t.set_font(FONT_FILE_BITMAP)
    t.toggle_show_cursor(True)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    t.gen_prompt(t.curr_row)
    t.gen_typing_text(
    "\x1b[92m# :(){ :|:& }; # now dream\x1b[0m",
    t.curr_row,
    contin=True,
)
    t.save_frame("fetch_details.png")
    t.gen_text("", t.curr_row, count=120, contin=True)

    t.gen_gif()
    image = gifos.utils.upload_imgbb("output.gif", 129600)  # 1.5 days expiration
    readme_file_content = rf"""<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="./output.gif">
    <source media="(prefers-color-scheme: light)" srcset="./output.gif">
    <img alt="GIFOS" src="output.gif">
</picture>

<sub><i>Inspired from [x0rzavi/github-readme-terminal](https://github.com/x0rzavi/github-readme-terminal)</i></sub>

<!-- <details>
<summary>More details</summary>

</details> -->
</div>

<!-- Image deletion URL: NONE -->"""
    with open("README.md", "w") as f:
        f.write(readme_file_content)
        print("INFO: README.md file generated")


if __name__ == "__main__":
    main()
