$skillsDir = "c:\Users\HP ZBOOK\Desktop\Skills for Antigravity\Skills for Claude\skills-claude"

$replacements = @{
    "\bthe next Claude\b" = "the Assistant"
    "\bClaude\b" = "the Assistant"
    "\bclaude\.ai\b" = "the browser"
    "\bClaude artifacts\b" = "standalone files"
    "\bRead tool\b" = "view_file tool"
    "\bWrite tool\b" = "write_to_file tool"
}

if (!(Test-Path $skillsDir)) {
    Write-Host "Directory not found: $skillsDir"
    exit
}

Get-ChildItem -Path $skillsDir -Recurse -Filter "SKILL.md" | ForEach-Object {
    $file = $_.FullName
    Write-Host "Migrating: $file"
    
    $content = Get-Content -Path $file -Raw -Encoding UTF8
    $originalContent = $content
    
    foreach ($pattern in $replacements.Keys) {
        $replacement = $replacements[$pattern]
        $content = $content -replace $pattern, $replacement
    }
    
    if ($content -ne $originalContent) {
        Set-Content -Path $file -Value $content -Encoding UTF8
        Write-Host "  -> Updated $file"
    } else {
        Write-Host "  -> No changes needed"
    }
}
