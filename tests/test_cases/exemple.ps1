<# 
  This is a powershell script that allows to upload background facts using the Rest API
#> 

$baseurl = "http://XXXX:8080/MyCustomer-AAD/rest"
$domain = "AAD"
$username = "user"
$password = ""
# Application id (in the Rest API)
$idapp = "1687"

Write-Output($username)
#Write-Output($password)

$base64AuthInfo = [Convert]::ToBase64String([Text.Encoding]::ASCII.GetBytes(("{0}:{1}" -f $username,$password)))
Write-Output($bas64AuthInfo)

#$idbkgmetrics = "66061"
$idbkgmetrics = "66061,66004,66005,66006,66007"

Write-Output('#####################################################################')
$idsnapshot = "535"
Write-Output('Snapshot R19-1 (' + $idsnapshot +')')
$url = $baseurl + '/' + $domain +'/applications/' + $idapp + '/snapshots/' + $idsnapshot + '/results?background-facts=('+$idbkgmetrics+')'
Write-Output('url='+$url)
Write-Output('Load data ...')
$body='ADG Database;Application Name;Module Name;Metric Id;Result
u101_cactus_2507_central;U-101 - Cactus;;66004;3025.4
u101_cactus_2507_central;U-101 - Cactus;PSFT DELTA;66004;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_ADDED;66004;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_MODIFIED;66004;1
u101_cactus_2507_central;U-101 - Cactus;;66005;713.3
u101_cactus_2507_central;U-101 - Cactus;PSFT DELTA;66005;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_ADDED;66005;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_MODIFIED;66005;1
u101_cactus_2507_central;U-101 - Cactus;;66006;2307.9
u101_cactus_2507_central;U-101 - Cactus;PSFT DELTA;66006;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_ADDED;66006;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_MODIFIED;66006;1
u101_cactus_2507_central;U-101 - Cactus;;66007;4.2
u101_cactus_2507_central;U-101 - Cactus;PSFT DELTA;66007;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_ADDED;66007;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_MODIFIED;66007;1
u101_cactus_2507_central;U-101 - Cactus;;66061;1
u101_cactus_2507_central;U-101 - Cactus;PSFT DELTA;66061;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_ADDED;66061;1
u101_cactus_2507_central;U-101 - Cactus;REPOSITORY_MODIFIED;66061;1'

Invoke-WebRequest -Uri "$url" -Method PUT -Headers @{"Authorization" = "Basic $base64AuthInfo" ; "Accept" = "*/*"} -Body $body -ContentType "text/csv"


<# 
  Call to an executable file
  https://social.technet.microsoft.com/wiki/contents/articles/7703.powershell-running-executables.aspx
#> 
.\MyEITest.exe

