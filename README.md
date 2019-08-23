# Microsoft Malware Prediction
by Juan Brugera Monedero and Javier Muñoz Alonso.

## 1. Introduction
Starting from the [Kaggle competition](https://www.kaggle.com/c/microsoft-malware-prediction/) we will try to achieve being in the top 120 [private leaderboard](https://www.kaggle.com/c/microsoft-malware-prediction/leaderboard) to win a silver medal.

In Kaggle, test data is not labeled, so the first thing we did was take a 10% of records from train to test and upload it to Dropbox in case these are no longer available.

Our process automatically dowloand them from Dropbox, but if you want to download yourself, you could do it from here:

[Train Data](https://www.dropbox.com/s/raw/26076osif4mgww8/train.csv.gz)
[Test Data](https://www.dropbox.com/s/raw/b8vztaybqzujm5w/test.csv.gz)

## 2. Requirements

All code in our process has been developed with python and third-party libraries, so the first thing you have to do is prepare an eviroment to be able to run all the code.

Don't worry, it's just as easy as follow the steps below.

Asuming you have ever installed [**Conda**](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) and [**JDK**](https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) (follow the links if not) you should run these commands in a Terminal (maybe bash):
````sh
conda create -n mimape python=3

conda activate mimape # source activate if conda version earlier than 4.6

conda install jupyter
conda install seaborn
conda install matplotlib
conda install scikit-learn
conda install xgboost
conda install pandas
conda install numpy
conda install pyspark
conda install requests
````
**P.S.**: Python3 own libraries as *warnings, itertools, logging and os* are also used in this code.

## 3. Code Explanation
The main code is at a Jupyter Notebook names as **Main.ipynb** and it's commented but there are another .py files to have in consideration.

* Utilities.py : Auxiliary functions that are used in the main process frequently.
* Spark.py : Apache Spark initialization for local runs.
* Resources.py : Pre-loaded variables collection.
* DataGetter.py, DataResources.py and Data.py : Auxiliary functions to download **Train** and **Test** from Dropbox.

## 4. Process Configuration
At the beginning of the process there is a configuration cell where you can configure certain parameters.

These are the most important (and the only should be modified):
````python
cv = 3 # Loops in data for cross validation searches
n_iter = 30 # Number of parameter settings that are sampled in RandomizedSearchCV
sample_size = .1 # train sample percentage due to the large volume of data
cut_at = .01 # variable weight (percentage) to be in model
````
## 5. Process
The goal of this competition is to predict a Windows machine’s probability of getting infected by various families of malware.

For this, we make use of classifiers as Decision Trees, Random Forest or XGBoost.

Our principal score will be the **Area Under the Curve ROC** but we will use also other scores like **precision, accuray or recall**.

### 5.1 Process Initialization
In this chapter, we perfom all the necessary code (like imports, configurations and some *defs*) to run the process.

### 5.2 Visualizing Data
At this point, we plot graphics for each variable and its values.
You will find it at *./Analysis.tgz*.

In our inexperienced opinion, due to the variety of values of each characteristic and its distribution, it was not worth transforming its values.

In fact, we tried, but we made all the scores worse during the process, so we finally dismissed these changes.

### 5.3 First Attemp
Due to a personal (bad) criterion, we decide fitting our model with features which contain less than 100 different values.

### 5.4 Coming Back
Being a bit more reasonable, we decided to create a correlation matrix and based on that try to improve the score of the metrics.

We did it, but we are not yet positioned in the ranking as we would like.

### 5.5 Trying with all
We decided to try all the features obtaining the weights of each of them for each of the models to finally take those with a relevance higher than 1% and perform the process with SparkML.

We also predict against test and we achieve a score of ~0.65.

### 5.6 After exploration, optimization
After obtaining certain conclusions, we launched the process with Spark and with those hyper parameters with which we hope to obtain better results.

## 6. Front-End
A reporting visualization tool with some statistics about process is available at [this link](http://tfmkschool2019.azurewebsites.net/).

It's interactive so you can pass the mouse over graphics and select or unselect the things you want to see clicking in the coloured circles.

## 7. Conclusions

Finally, we get a ~0.68 score, meaning we reach the top 1 position in the [private leaderboard](https://www.kaggle.com/c/microsoft-malware-prediction/leaderboard). We are really proud of this fact, even more considering competition difficulty and the complexity of the data.

We are also satisfied with the tools and knowledge acquired about them.

We want to thank the entire faculty of the K-School for the time and patience spent in us, especially [Daniel Mateos](https://github.com/danimateos) and [Sebastien Perez Vasseur](https://github.com/rezpe) who have guided and cared for us throughout the course, even after class hours.

## 8. Additional Information
1. SparkConf for running local process can be changed in Spark.py.
2. Some information from Main.ipynb may not match with the presented here due to a final run with a 1% (instead of 10%) sample from train.

## 9. Raw Data Description
Unavailable or self-documenting column names are marked with an "NA".

1. MachineIdentifier- Individual machine ID
2. ProductName- Defender state information e.g. win8defender
3. EngineVersion- Defender state information e.g. 1.1.12603.0
4. AppVersion- Defender state information e.g. 4.9.10586.0
5. AvSigVersion- Defender state information e.g. 1.217.1014.0
6. IsBeta- Defender state information e.g. false
7. RtpStateBitfield- NA
8. IsSxsPassiveMode- NA
9. DefaultBrowsersIdentifier- ID for the machine's default browser
10. AVProductStatesIdentifier- ID for the specific configuration of a user's antivirus software
11. AVProductsInstalled- NA
12. AVProductsEnabled- NA
13. HasTpm- True if machine has tpm
14. CountryIdentifier- ID for the country the machine is located in
15. CityIdentifier- ID for the city the machine is located in
16. OrganizationIdentifier- ID for the organization the machine belongs in, organization ID is mapped to both specific companies and broad industries
17. GeoNameIdentifier- ID for the geographic region a machine is located in
18. LocaleEnglishNameIdentifier- English name of Locale ID of the current user
19. Platform- Calculates platform name (of OS related properties and processor property)
20. Processor- This is the process architecture of the installed operating system
21. OsVer- Version of the current operating system
22. OsBuild- Build of the current operating system
23. OsSuite- Product suite mask for the current operating system.
24. OsPlatformSubRelease- Returns the OS Platform sub-release (Windows Vista, Windows 7, Windows 8, TH1, TH2)
25. OsBuildLab- Build lab that generated the current OS. Example: 9600.17630.amd64fre.winblue_r7.150109-2022
26. SkuEdition- The goal of this feature is to use the Product Type defined in the MSDN to map to a 'SKU-Edition' name that is useful in population reporting. The valid Product Type are defined in %sdxroot%\data\windowseditions.xml. This API has been used since Vista and Server 2008, so there are many Product Types that do not apply to Windows 10. The 'SKU-Edition' is a string value that is in one of three classes of results. The design must hand each class.
27. IsProtected- This is a calculated field derived from the Spynet Report's AV Products field. Returns: a. TRUE if there is at least one active and up-to-date antivirus product running on this machine. b. FALSE if there is no active AV product on this machine, or if the AV is active, but is not receiving the latest updates. c. null if there are no Anti Virus Products in the report. Returns: Whether a machine is protected.
28. AutoSampleOptIn- This is the SubmitSamplesConsent value passed in from the service, available on CAMP 9+
29. PuaMode- Pua Enabled mode from the service
30. SMode- This field is set to true when the device is known to be in 'S Mode', as in, Windows 10 S mode, where only Microsoft Store apps can be installed
31. IeVerIdentifier- NA
32. SmartScreen- This is the SmartScreen enabled string value from registry. This is obtained by checking in order, HKLM\SOFTWARE\Policies\Microsoft\Windows\System\SmartScreenEnabled and HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\SmartScreenEnabled. If the value exists but is blank, the value "ExistsNotSet" is sent in telemetry.
33. Firewall- This attribute is true (1) for Windows 8.1 and above if windows firewall is enabled, as reported by the service.
34. UacLuaenable- This attribute reports whether or not the "administrator in Admin Approval Mode" user type is disabled or enabled in UAC. The value reported is obtained by reading the regkey HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\EnableLUA.
35. Census_MDC2FormFactor- A grouping based on a combination of Device Census level hardware characteristics. The logic used to define Form Factor is rooted in business and industry standards and aligns with how people think about their device. (Examples: Smartphone, Small Tablet, All in One, Convertible...)
36. Census_DeviceFamily- AKA DeviceClass. Indicates the type of device that an edition of the OS is intended for. Example values: Windows.Desktop, Windows.Mobile, and iOS.Phone
37. Census_OEMNameIdentifier- NA
38. Census_OEMModelIdentifier- NA
39. Census_ProcessorCoreCount- Number of logical cores in the processor
40. Census_ProcessorManufacturerIdentifier- NA
41. Census_ProcessorModelIdentifier- NA
42. Census_ProcessorClass- A classification of processors into high/medium/low. Initially used for Pricing Level SKU. No longer maintained and updated
43. Census_PrimaryDiskTotalCapacity- Amount of disk space on primary disk of the machine in MB
44. Census_PrimaryDiskTypeName- Friendly name of Primary Disk Type - HDD or SSD
45. Census_SystemVolumeTotalCapacity- The size of the partition that the System volume is installed on in MB
46. Census_HasOpticalDiskDrive- True indicates that the machine has an optical disk drive (CD/DVD)
47. Census_TotalPhysicalRAM- Retrieves the physical RAM in MB
48. Census_ChassisTypeName- Retrieves a numeric representation of what type of chassis the machine has. A value of 0 means xx
49. Census_InternalPrimaryDiagonalDisplaySizeInInches- Retrieves the physical diagonal length in inches of the primary display
50. Census_InternalPrimaryDisplayResolutionHorizontal- Retrieves the number of pixels in the horizontal direction of the internal display.
51. Census_InternalPrimaryDisplayResolutionVertical- Retrieves the number of pixels in the vertical direction of the internal display
52. Census_PowerPlatformRoleName- Indicates the OEM preferred power management profile. This value helps identify the basic form factor of the device
53. Census_InternalBatteryType- NA
54. Census_InternalBatteryNumberOfCharges- NA
55. Census_OSVersion- Numeric OS version Example - 10.0.10130.0
56. Census_OSArchitecture- Architecture on which the OS is based. Derived from OSVersionFull. Example - amd64
57. Census_OSBranch- Branch of the OS extracted from the OsVersionFull. Example - OsBranch = fbl_partner_eeap where OsVersion = 6.4.9813.0.amd64fre.fbl_partner_eeap.140810-0005
58. Census_OSBuildNumber- OS Build number extracted from the OsVersionFull. Example - OsBuildNumber = 10512 or 10240
59. Census_OSBuildRevision- OS Build revision extracted from the OsVersionFull. Example - OsBuildRevision = 1000 or 16458
60. Census_OSEdition- Edition of the current OS. Sourced from HKLM\Software\Microsoft\Windows NT\CurrentVersion@EditionID in registry. Example: Enterprise
61. Census_OSSkuName- OS edition friendly name (currently Windows only)
62. Census_OSInstallTypeName- Friendly description of what install was used on the machine i.e. clean
63. Census_OSInstallLanguageIdentifier- NA
64. Census_OSUILocaleIdentifier- NA
65. Census_OSWUAutoUpdateOptionsName- Friendly name of the WindowsUpdate auto-update settings on the machine.
66. Census_IsPortableOperatingSystem- Indicates whether OS is booted up and running via Windows-To-Go on a USB stick.
67. Census_GenuineStateName- Friendly name of OSGenuineStateID. 0 = Genuine
68. Census_ActivationChannel- Retail license key or Volume license key for a machine.
69. Census_IsFlightingInternal- NA
70. Census_IsFlightsDisabled- Indicates if the machine is participating in flighting.
71. Census_FlightRing- The ring that the device user would like to receive flights for. This might be different from the ring of the OS which is currently installed if the user changes the ring after getting a flight from a different ring.
72. Census_ThresholdOptIn- NA
73. Census_FirmwareManufacturerIdentifier- NA
74. Census_FirmwareVersionIdentifier- NA
75. Census_IsSecureBootEnabled- Indicates if Secure Boot mode is enabled.
76. Census_IsWIMBootEnabled- NA
77. Census_IsVirtualDevice- Identifies a Virtual Machine (machine learning model)
78. Census_IsTouchEnabled- Is this a touch device ?
79. Census_IsPenCapable- Is the device capable of pen input ?
80. Census_IsAlwaysOnAlwaysConnectedCapable- Retreives information about whether the battery enables the device to be AlwaysOnAlwaysConnected.
81. Wdft_IsGamer- Indicates whether the device is a gamer device or not based on its hardware combination.
82. Wdft_RegionIdentifier- NA
83. **HasDetections** is the ground truth and indicates that Malware was detected on the machine.
