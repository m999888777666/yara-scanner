rule RansomwareRule{
    strings:
        $ransom_note="Your files are encrypted" nocase
    condition:
        $ransom_note
}