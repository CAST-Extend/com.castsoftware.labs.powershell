# ============================================
# Analytics Tools Module
# ============================================

function Get-Average {
    param([double[]]$Numbers)
    $sum = 0
    foreach ($n in $Numbers) { $sum += $n }
    return $sum / $Numbers.Length
}

function Get-Median {
    param([double[]]$Numbers)
    $sorted = $Numbers | Sort-Object
    $middle = [math]::Floor($sorted.Length / 2)
    if ($sorted.Length % 2) {
        return $sorted[$middle]
    } else {
        return ($sorted[$middle - 1] + $sorted[$middle]) / 2
    }
}

class DataAnalyzer {
    [double[]]$Data

    DataAnalyzer([double[]]$values) {
        $this.Data = $values
    }

    [void]ShowReport() {
        $avg = Get-Average $this.Data
        $med = Get-Median $this.Data
        Write-Host "Average: $avg | Median: $med"
    }
}

# Example usage
$data = @(1.5, 2.3, 4.8, 3.1, 2.0)
$analyzer = [DataAnalyzer]::new($data)
$analyzer.ShowReport()
