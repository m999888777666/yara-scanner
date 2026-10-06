rule SampleRule{
    strings:
        $secret_text="malware" nocase
    condition:
        $secret_text
}