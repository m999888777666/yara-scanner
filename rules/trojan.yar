rule TrojanSample {
    strings:
        $trojan_str = "malware_test"
    condition:
        $trojan_str
}