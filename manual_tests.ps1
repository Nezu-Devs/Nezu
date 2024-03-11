
'------------------------------------'
'              example               '
'------------------------------------'
python -m nezu.manual_tests.ztest_example

'------------------------------------'
'              seek 1                '
'------------------------------------'
$env:NEZU_SEEK=1
py -m nezu.manual_tests.ztest_hide
'------------------------------------'
'              seek 3                '
'------------------------------------'
$env:NEZU_SEEK=3
py -m nezu.manual_tests.ztest_hide
'------------------------------------'
'              seek 5                '
'------------------------------------'
$env:NEZU_SEEK=5
py -m nezu.manual_tests.ztest_hide
'------------------------------------'
'                nez                 '
'------------------------------------'
$env:NEZU_SEEK=5
py -m nezu.manual_tests.ztest_nez