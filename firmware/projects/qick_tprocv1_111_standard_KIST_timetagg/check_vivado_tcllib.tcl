puts "vivado=[version -short]"
set packages [list math::bignum yaml]
foreach pkg $packages {
    if {[catch {package require $pkg} err]} {
        puts "PKG_FAIL $pkg: $err"
        exit 1
    } else {
        puts "PKG_OK $pkg"
    }
}
exit 0
