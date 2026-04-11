A step-by-step guide to setting up a personal Product Marketing knowledge base using Obsidian, Git, and Claude Code.
# What You're Building
A structured, compounding wiki for Product Marketing Management knowledge — frameworks, competitive intel, analyst relationships, messaging, and reusable workflows. It lives in Obsidian for daily use and Claude Code for AI-powered ingestion, querying, and content generation.

This is the "LLM Wiki" pattern (inspired by Andrej Karpathy's approach): a knowledge base that gets smarter every time you feed it a source, and that an LLM can reason over on demand.
# What You'll Need
- A computer (macOS, Windows, or Linux)
- An Anthropic account with Claude Pro or Team (for Claude Code access)
- About 30 minutes for initial setup
## Step 1: Install Obsidian
Obsidian is a free, local-first markdown editor. Your wiki lives as plain `.md` files on your machine — no vendor lock-in.

1. Go to [obsidian.md](https://obsidian.md/) and download the installer for your OS.
2. Run the installer.
3. When Obsidian opens, choose **Create new vault**.
4. Name it something like `pmm-brain`.
5. Pick a location you'll remember (e.g., `~/Documents/pmm-brain` on Mac/Linux, or `C:\Users\YourName\Documents\pmm-brain` on Windows).
6. Click **Create**.

You now have an empty vault. Leave Obsidian open — we'll come back to it.
## Step 2: Install Git
Git tracks every change to your wiki, lets you roll back mistakes, and keeps a clean history.

**macOS:**
```bash
# If you have Homebrew:
brew install git

# Or install Xcode Command Line Tools (includes git):
xcode-select --install
```

**Windows:** Download and install [Git for Windows](https://gitforwindows.org/). Use the default settings. This gives you Git Bash, which you'll use for terminal commands.

**Linux:**
```bash
sudo apt install git    # Debian/Ubuntu
sudo dnf install git    # Fedora
```

Verify it works:
```bash
git --version
```

## Step 3: Install the Obsidian Git Plugin
This lets you commit and push changes from inside Obsidian without touching the terminal.

1. In Obsidian, open **Settings** (gear icon, bottom-left).
2. Go to **Community plugins**.
3. If prompted, click **Turn on community plugins**.
4. Click **Browse** and search for **Obsidian Git**.
5. Click **Install**, then **Enable**.
6. Go to the plugin's settings (under Community plugins → Obsidian Git → gear icon).
7. Configure auto-backup interval if you want automatic commits (e.g., every 30 minutes). Or leave it manual — your call.

Don't worry about connecting to a remote repo yet. The plugin works fine for local commits, and you can add a GitHub/GitLab remote later if you want cloud backup.

## Step 4: Install Claude Code
Claude Code is a CLI tool that lets Claude operate directly in your filesystem — reading files, creating pages, running your wiki workflows.

**Prerequisites:** Node.js 18+ must be installed.
- **macOS/Linux:** Install Node via [nodejs.org](https://nodejs.org/) or your package manager.
- **Windows:** Install Node from [nodejs.org](https://nodejs.org/). Use the LTS version.

Then install Claude Code:
```bash
npm install -g @anthropic-ai/claude-code
```

Verify:
```bash
claude --version
```

On first run, Claude Code will prompt you to authenticate with your Anthropic account.
## Step 5: Bootstrap Your Wiki
This is where the magic happens. You'll paste a single prompt into Claude Code and it will scaffold your entire knowledge base structure.

1. Open a terminal.
2. Navigate to your vault directory:
    
    ```bash
    cd ~/Documents/pmm-brain    # adjust to your vault path
    ```
    
3. Start Claude Code:
    
    ```bash
    claude
    ```
    
1. Copy and Paste the entire contents of the [[Bootstrap]] prompt file into Claude Code.
2. Let Claude Code run. It will create your folder structure, CLAUDE.md, starter skills, templates, and initialize git.
3. When it finishes, switch to Obsidian. Your vault should now be populated with the full wiki scaffold.

## Step 6: Verify and First Commit
1. In Obsidian, you should see the folder structure in the left sidebar: `wiki/`, `skills/`, `templates/`, `examples/`, `raw/`.
2. Open `CLAUDE.md` and review it — this is Claude's instruction manual for your vault.
3. Open `wiki/index.md` — your master index (currently empty, will grow as you add content).
4. When you're satisfied, make your first commit:
    - Use the Obsidian Git plugin: open the command palette (`Cmd/Ctrl + P`), search for **Obsidian Git: Create backup**, and run it.
    - Or from the terminal: `git add -A && git commit -m "scaffold: initial pmm-brain setup"`

## Using Your Wiki
Once scaffolded, start a Claude Code session in your vault directory and use the slash commands:

| Command                 | What It Does                                                                                             |
| ----------------------- | -------------------------------------------------------------------------------------------------------- |
| `/ingest [source]`      | Feed a source into the wiki — creates source summaries, extracts entities and concepts, links everything |
| `/query [question]`     | Ask a question answered from your wiki's knowledge, not generic training data                            |
| `/build [skill] [args]` | Generate an output (battle card, messaging framework, etc.) using your wiki as context                   |
| `/lint`                 | Find orphan pages, dead links, missing frontmatter, stale content                                        |
| `/status`               | See wiki stats, recent activity, current context                                                         |

**Example first session:**

```
> /ingest raw/forrester-wave-dpa-2024.pdf
> /query What are the key differentiators Forrester identified for leaders in DPA?
> /build battle-card --competitor Appian
```

## Bootstrap Prompt
Copy the contents of the [[Bootstrap]] file and paste it into Claude Code.

# Tips
- **Start by ingesting sources you already have.** Drop PDFs, analyst reports, or competitor blog posts into `raw/` and run `/ingest`. The wiki compounds fast.
- **Use `/query` instead of asking Claude generic questions.** It forces answers grounded in _your_ knowledge base, not training data.
- **Run `/lint` periodically.** It catches dead links, orphan pages, and stale content before they become a mess.
- **Fork for your company.** Once you have a solid base of generic PMM knowledge, create a `company/` directory and start adding company-specific positioning, competitive intel, and analyst relationships.
- **Commit often.** Even if you're not pushing to a remote, local git history is your undo button.

# FAQ
**Do I need a GitHub/GitLab account?** No. Git works locally. A remote repo is optional but recommended for backup.

**Can I use this with a different LLM tool instead of Claude Code?** The Obsidian vault works standalone — it's just markdown files. The slash commands and CLAUDE.md are specific to Claude Code, but the structure and conventions are portable.

**What if I already have a PMM knowledge base?** Drop your existing content into `raw/` and use `/ingest` to process it into the wiki structure. You can also manually create pages in the wiki folders following the frontmatter schemas.

**Does this work on Windows?** Yes. Use Git Bash or Windows Terminal for CLI commands. All paths in the bootstrap use forward slashes, which work in both Git Bash and Claude Code on Windows.