# Kschool-TFM

## Versions

Python Version: 3.6

Spark Version: 2.4.1

## Input Definition

### Columns
Unavailable or self-documenting column names are marked with an "NA".

1. MachineIdentifier - Individual machine ID
2. ProductName - Defender state information e.g. win8defender
3. EngineVersion - Defender state information e.g. 1.1.12603.0
4. AppVersion - Defender state information e.g. 4.9.10586.0
5. AvSigVersion - Defender state information e.g. 1.217.1014.0
6. IsBeta - Defender state information e.g. false
7. RtpStateBitfield - NA
8. IsSxsPassiveMode - NA
9. DefaultBrowsersIdentifier - ID for the machine's default browser
10. AVProductStatesIdentifier - ID for the specific configuration of a user's antivirus software
11. AVProductsInstalled - NA
12. AVProductsEnabled - NA
13. HasTpm - True if machine has tpm
14. CountryIdentifier - ID for the country the machine is located in
15. CityIdentifier - ID for the city the machine is located in
16. OrganizationIdentifier - ID for the organization the machine belongs in, organization ID is mapped to both specific companies and broad industries
17. GeoNameIdentifier - ID for the geographic region a machine is located in
18. LocaleEnglishNameIdentifier - English name of Locale ID of the current user
19. Platform - Calculates platform name (of OS related properties and processor property)
20. Processor - This is the process architecture of the installed operating system
21. OsVer - Version of the current operating system
22. OsBuild - Build of the current operating system
23. OsSuite - Product suite mask for the current operating system.
24. OsPlatformSubRelease - Returns the OS Platform sub-release (Windows Vista, Windows 7, Windows 8, TH1, TH2)
25. OsBuildLab - Build lab that generated the current OS. Example: 9600.17630.amd64fre.winblue_r7.150109-2022
26. SkuEdition - The goal of this feature is to use the Product Type defined in the MSDN to map to a 'SKU-Edition' name that is useful in population reporting. The valid Product Type are defined in %sdxroot%\data\windowseditions.xml. This API has been used since Vista and Server 2008, so there are many Product Types that do not apply to Windows 10. The 'SKU-Edition' is a string value that is in one of three classes of results. The design must hand each class.
27. IsProtected - This is a calculated field derived from the Spynet Report's AV Products field. Returns: a. TRUE if there is at least one active and up-to-date antivirus product running on this machine. b. FALSE if there is no active AV product on this machine, or if the AV is active, but is not receiving the latest updates. c. null if there are no Anti Virus Products in the report. Returns: Whether a machine is protected.
28. AutoSampleOptIn - This is the SubmitSamplesConsent value passed in from the service, available on CAMP 9+
29. PuaMode - Pua Enabled mode from the service
30. SMode - This field is set to true when the device is known to be in 'S Mode', as in, Windows 10 S mode, where only Microsoft Store apps can be installed
31. IeVerIdentifier - NA
32. SmartScreen - This is the SmartScreen enabled string value from registry. This is obtained by checking in order, HKLM\SOFTWARE\Policies\Microsoft\Windows\System\SmartScreenEnabled and HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\SmartScreenEnabled. If the value exists but is blank, the value "ExistsNotSet" is sent in telemetry.
33. Firewall - This attribute is true (1) for Windows 8.1 and above if windows firewall is enabled, as reported by the service.
34. UacLuaenable - This attribute reports whether or not the "administrator in Admin Approval Mode" user type is disabled or enabled in UAC. The value reported is obtained by reading the regkey HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\EnableLUA.
35. Census_MDC2FormFactor - A grouping based on a combination of Device Census level hardware characteristics. The logic used to define Form Factor is rooted in business and industry standards and aligns with how people think about their device. (Examples: Smartphone, Small Tablet, All in One, Convertible...)
36. Census_DeviceFamily - AKA DeviceClass. Indicates the type of device that an edition of the OS is intended for. Example values: Windows.Desktop, Windows.Mobile, and iOS.Phone
37. Census_OEMNameIdentifier - NA
38. Census_OEMModelIdentifier - NA
39. Census_ProcessorCoreCount - Number of logical cores in the processor
40. Census_ProcessorManufacturerIdentifier - NA
41. Census_ProcessorModelIdentifier - NA
42. Census_ProcessorClass - A classification of processors into high/medium/low. Initially used for Pricing Level SKU. No longer maintained and updated
43. Census_PrimaryDiskTotalCapacity - Amount of disk space on primary disk of the machine in MB
44. Census_PrimaryDiskTypeName - Friendly name of Primary Disk Type - HDD or SSD
45. Census_SystemVolumeTotalCapacity - The size of the partition that the System volume is installed on in MB
46. Census_HasOpticalDiskDrive - True indicates that the machine has an optical disk drive (CD/DVD)
47. Census_TotalPhysicalRAM - Retrieves the physical RAM in MB
48. Census_ChassisTypeName - Retrieves a numeric representation of what type of chassis the machine has. A value of 0 means xx
49. Census_InternalPrimaryDiagonalDisplaySizeInInches - Retrieves the physical diagonal length in inches of the primary display
50. Census_InternalPrimaryDisplayResolutionHorizontal - Retrieves the number of pixels in the horizontal direction of the internal display.
51. Census_InternalPrimaryDisplayResolutionVertical - Retrieves the number of pixels in the vertical direction of the internal display
52. Census_PowerPlatformRoleName - Indicates the OEM preferred power management profile. This value helps identify the basic form factor of the device
53. Census_InternalBatteryType - NA
54. Census_InternalBatteryNumberOfCharges - NA
55. Census_OSVersion - Numeric OS version Example - 10.0.10130.0
56. Census_OSArchitecture - Architecture on which the OS is based. Derived from OSVersionFull. Example - amd64
57. Census_OSBranch - Branch of the OS extracted from the OsVersionFull. Example - OsBranch = fbl_partner_eeap where OsVersion = 6.4.9813.0.amd64fre.fbl_partner_eeap.140810-0005
58. Census_OSBuildNumber - OS Build number extracted from the OsVersionFull. Example - OsBuildNumber = 10512 or 10240
59. Census_OSBuildRevision - OS Build revision extracted from the OsVersionFull. Example - OsBuildRevision = 1000 or 16458
60. Census_OSEdition - Edition of the current OS. Sourced from HKLM\Software\Microsoft\Windows NT\CurrentVersion@EditionID in registry. Example: Enterprise
61. Census_OSSkuName - OS edition friendly name (currently Windows only)
62. Census_OSInstallTypeName - Friendly description of what install was used on the machine i.e. clean
63. Census_OSInstallLanguageIdentifier - NA
64. Census_OSUILocaleIdentifier - NA
65. Census_OSWUAutoUpdateOptionsName - Friendly name of the WindowsUpdate auto-update settings on the machine.
66. Census_IsPortableOperatingSystem - Indicates whether OS is booted up and running via Windows-To-Go on a USB stick.
67. Census_GenuineStateName - Friendly name of OSGenuineStateID. 0 = Genuine
68. Census_ActivationChannel - Retail license key or Volume license key for a machine.
69. Census_IsFlightingInternal - NA
70. Census_IsFlightsDisabled - Indicates if the machine is participating in flighting.
71. Census_FlightRing - The ring that the device user would like to receive flights for. This might be different from the ring of the OS which is currently installed if the user changes the ring after getting a flight from a different ring.
72. Census_ThresholdOptIn - NA
73. Census_FirmwareManufacturerIdentifier - NA
74. Census_FirmwareVersionIdentifier - NA
75. Census_IsSecureBootEnabled - Indicates if Secure Boot mode is enabled.
76. Census_IsWIMBootEnabled - NA
77. Census_IsVirtualDevice - Identifies a Virtual Machine (machine learning model)
78. Census_IsTouchEnabled - Is this a touch device ?
79. Census_IsPenCapable - Is the device capable of pen input ?
80. Census_IsAlwaysOnAlwaysConnectedCapable - Retreives information about whether the battery enables the device to be AlwaysOnAlwaysConnected.
81. Wdft_IsGamer - Indicates whether the device is a gamer device or not based on its hardware combination.
82. Wdft_RegionIdentifier - NA
83. **HasDetections** is the ground truth and indicates that Malware was detected on the machine.