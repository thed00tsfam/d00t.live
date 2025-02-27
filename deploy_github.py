import os
import subprocess

# GitHub repo details
GITHUB_USERNAME = "thed00tsfam"
REPO_NAME = "d00t.live"
VIDEO_FILE = "video.mp4"
HTML_FILE = "index.html"

# Generate the HTML file
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>d00t.live</title>
    <style>
        body, html {{
            margin: 0;
            padding: 0;
            overflow: hidden;
            background: black;
        }}
        video {{
            position: absolute;
            top: 50%;
            left: 50%;
            width: 100vw;
            height: 100vh;
            object-fit: cover;
            transform: translate(-50%, -50%);
        }}
    </style>
</head>
<body>
    <video autoplay muted loop playsinline>
        <source src="{VIDEO_FILE}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</body>
</html>"""

# Save HTML file
with open(HTML_FILE, "w") as f:
    f.write(html_content)

# Check if video file exists
if not os.path.exists(VIDEO_FILE):
    print(f"⚠️ Error: {VIDEO_FILE} not found! Place your video in the project folder.")
    exit(1)

# Git commands to push the files
commands = [
    "git add .",
    'git commit -m "Deploy website"',
    "git branch -M main",
    f"git remote add origin https://github.com/{GITHUB_USERNAME}/{REPO_NAME}.git",
    "git push -u origin main"
]

# Execute Git commands
for cmd in commands:
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git command failed: {cmd}\nError: {e}")
        exit(1)

print("\n✅ Deployment Complete!")
print("🌎 Your website will be live at: https://thed00tsfam.github.io/d00t.live")
print("\n🔧 Next Steps:")
print("- In your GitHub repo, go to 'Settings' → 'Pages'")
print("- Set the branch to 'main' and directory to '/'")
print("- Add 'd00t.live' as a custom domain in GitHub Pages settings")

