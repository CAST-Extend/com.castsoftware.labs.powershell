# exemple7.psm1
# Pure custom code only

class User {
    [string] $Name

    User([string]$name) {
        $this.Name = $name
    }

    [string] BuildGreeting() {
        $msg = "GreetingFrom_" + $this.Name
        return $msg
    }

    [string] BuildInternalData() {
        $data = "InternalData_" + $this.Name
        return $data
    }
}

function Get-CustomVersion {
    $v = "CustomVersion_1_0"
    return $v
}

Export-ModuleMember -Function Get-CustomVersion -Class User
