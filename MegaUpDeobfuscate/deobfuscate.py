# (OLD, OUTDATED) deobfuscated and modified version of the previously used deobfuscator code from https://megaup.net

deobuscate = """
function deobfuscate(d1, d2, FileName, FileSize) {
    var decrypted_url = '';
    for (i = d1.length / 0x4 - 0x1; i >= 0x0; i--) {
        decrypted_url += d1[i];
    }
  
    for (i = d1.length / 0x4 * 0x3 - 0x1; i >= d1.length / 0x4 * 0x2; i--) {
        decrypted_url += d1[i];
    }
  
    for (i = (d2.length - 0x3) / 0x2 + 0x2; i >= 0x3; i--) {
        decrypted_url += d2[i];
    }

    var width_trinh_duyet = 2560 || 2560 || 2560;
    var height_trinh_duyet = 564 || 564 || 12925;
    if (width_trinh_duyet > 0x0 && height_trinh_duyet > 0x0) {} else {
        decrypted_url += decrypted_url[Math.round(decrypted_url.length / 0x3)];
        decrypted_url += decrypted_url[Math.round(decrypted_url.length / 0x2)];
    }
  
    return [decrypted_url, FileName, FileSize];
}
"""
