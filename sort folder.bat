Get-ChildItem -Directory | ForEach-Object {
    $size = (Get-ChildItem $_.FullName -Recurse | Measure-Object -Property Length -Sum).Sum
    [PSCustomObject]@{
        'Folder' = $_.FullName
        'Size'   = $size / 1MB
    }
} | Sort-Object Size -Descending | Format-Table -AutoSize
