# ⚓ [Hanwha Ocean AX Portfolio] GitHub One-Click Push Script

Write-Host "🚀 Starting Enterprise GitHub Deployment: v1.0" -ForegroundColor Cyan

# 1. Check if Git is installed
if (!(Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "❌ Error: Git is not installed on this system." -ForegroundColor Red
    Write-Host "Please install Git from https://git-scm.com/ and try again."
    Read-Host "Press Enter to exit..."
    exit
}

# 2. Project Directory
$ProjectDir = $PSScriptRoot
Set-Location $ProjectDir

Write-Host "📂 Current Directory: $ProjectDir"

# 3. Git Initialization
if (!(Test-Path ".git")) {
    Write-Host "⚙️ Initializing Git Repository..."
    git init
}

# 4. Configuration
$RemoteUrl = "https://github.com/glory903-devsecops/hanwha-ocean-asset-monitor.git"

# Check if remote exists, if not add it
$existingRemote = git remote get-url origin 2>$null
if ($null -eq $existingRemote) {
    Write-Host "🔗 Adding Remote Origin: $RemoteUrl"
    git remote add origin $RemoteUrl
} else {
    Write-Host "🔗 Remote Origin already exists: $existingRemote"
}

# 5. Commit and Push
Write-Host "📦 Adding files and committing..."
git add .
git commit -m "feat: Initial Enterprise AX Monitoring System v1.0 [Premium Portfolio]"

Write-Host "📤 Pushing to GitHub (A login window may appear)..."
git branch -M main
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ SUCCESS: Your portfolio is now LIVE on GitHub!" -ForegroundColor Green
    Write-Host "URL: $RemoteUrl"
} else {
    Write-Host "`n❌ FAILED: There was an issue pushing the code. Check your credentials." -ForegroundColor Red
}

Read-Host "`nPress Enter to close this window..."
