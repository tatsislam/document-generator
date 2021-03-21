# Specification for Embedded Subsystem  
  
### Table of Contents  
  * [Specification for Embedded Subsystem](#specification-for-embedded-subsystem)
    * [7.8 Turning Signal Information](#78-turning-signal-information)
    * [7.7 Speed Information](#77-speed-information)
    * [7.9 Hazard Light Information](#79-hazard-light-information)
    * [7.10 Energy Storage Warning Information](#710-energy-storage-warning-information)
    * [10.1 Cruise Control Deactivation](#101-cruise-control-deactivation)
    * [12.3.1 Acceleration](#1231-acceleration)
    * [12.3.2 Braking](#1232-braking)
    * [12.3.3 Daytime running lights ](#1233-daytime-running-lights-)
    * [12.3.5 High beam lights](#1235-high-beam-lights)
    * [12.3.6 Fog lights ](#1236-fog-lights-)
    * [12.3.7 Tail lights](#1237-tail-lights)
    * [12.3.8 Illuminate number plate](#1238-illuminate-number-plate)
    * [12.3.9 Brake lights](#1239-brake-lights)
    * [12.3.10 Indicators - front](#12310-indicators---front)
    * [12.3.11 Indicators - side ](#12311-indicators---side-)
    * [12.3.12 Indicators - back](#12312-indicators---back)
    * [12.3.13 Hazard lights](#12313-hazard-lights)
    * [12.3.14 Interior lights](#12314-interior-lights)
    * [12.3.15 Horn](#12315-horn)
    * [12.3.16 Front brake pressure](#12316-front-brake-pressure)
    * [12.3.17 Rear brake pressure](#12317-rear-brake-pressure)
    * [12.3.18 Solar pyranometer](#12318-solar-pyranometer)
    * [12.3.19 GPS position](#12319-gps-position)
    * [12.3.20 Cabin temperature ](#12320-cabin-temperature-)
    * [12.3.21 Cabin humidity](#12321-cabin-humidity)
    * [12.3.22 Panel temperature ](#12322-panel-temperature-)
    * [12.3.23 High power bus voltage/current](#12323-high-power-bus-voltagecurrent)
    * [12.3.24 Low power bus voltage/current](#12324-low-power-bus-voltagecurrent)
    * [12.3.25 Tyre pressure](#12325-tyre-pressure)
    * [12.3.26 Acceleration](#12326-acceleration)
    * [12.3.27 Compas direction](#12327-compas-direction)
    * [12.3.28 Gyroscope data ](#12328-gyroscope-data-)
    * [12.3.29 Motor monitoring ](#12329-motor-monitoring-)

## 7.8 Turning Signal Information  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Turning signal information, i.e. whether it is on or off, must be displayed to the driver while they are driving | IMP |  |  
  
  
## 7.7 Speed Information  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| The speed of the vehicle must always be displayed to the driver while they are driving | IMP |  |  
  
  
## 7.9 Hazard Light Information  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Hazard light information, i.e. whether they are on or off, must be displayed to the driver while they are driving. | IMP |  |  
  
  
## 7.10 Energy Storage Warning Information  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| All battery system warnings should be displayed to the driver when they are driving. | IMP |  |  
  
  
## 10.1 Cruise Control Deactivation  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Cruise control must automatically deactivate when the brake is operated, or the car is turned off.  | IMP | Open |  
  
  
## 12.3.1 Acceleration  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the physical movement of the car in regard to acceleration.  | 1 | Open |  
  
  
## 12.3.2 Braking  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the physical movement of the car in regard to braking.  | 1 | Open |  
  
  
## 12.3.3 Daytime running lights   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the daytime running lights. | 1 | Open |  
  
  
## 12.3.5 High beam lights  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the high beam lights | 2 | Open |  
  
  
## 12.3.6 Fog lights   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the fog lights | 2 | Open |  
  
  
## 12.3.7 Tail lights  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the tail lights | 1 | Open |  
  
  
## 12.3.8 Illuminate number plate  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the number plate illuminator  | 1 | Open |  
  
  
## 12.3.9 Brake lights  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the 3 brake lights  | 1 | Open |  
  
  
## 12.3.10 Indicators - front  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the front indicators  | 1 | Open |  
  
  
## 12.3.11 Indicators - side   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the side indicators | 1 | Open |  
  
  
## 12.3.12 Indicators - back  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the back indicators  | 1 | Open |  
  
  
## 12.3.13 Hazard lights  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the hazard lights

 | 1 | Open |  
  
  
## 12.3.14 Interior lights  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the interior lights  | 3 | Open |  
  
  
## 12.3.15 Horn  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the horn  | 1 | Open |  
  
  
## 12.3.16 Front brake pressure  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the front brake pressure sensor.  | 1 | Open |  
  
  
## 12.3.17 Rear brake pressure  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the rear brake pressure sensor.  | 1 | Open |  
  
  
## 12.3.18 Solar pyranometer  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the solar pyranometer sensor.  | 1 | Open |  
  
  
## 12.3.19 GPS position  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the GPS position sensor.  | 1 | Open |  
  
  
## 12.3.20 Cabin temperature   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the cabin temperature sensor.  | 3 | Open |  
  
  
## 12.3.21 Cabin humidity  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the cabin humidity sensor.  | 3 | Open |  
  
  
## 12.3.22 Panel temperature   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the panel temperature sensor.  | 3 | Open |  
  
  
## 12.3.23 High power bus voltage/current  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the high power bus voltage/current sensor.  | 1 | Open |  
  
  
## 12.3.24 Low power bus voltage/current  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the low power bus voltage/current sensor.  | 1 | Open |  
  
  
## 12.3.25 Tyre pressure  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the 4 tyre pressure sensors.  | 1 | Open |  
  
  
## 12.3.26 Acceleration  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the acceleration sensor.  | 1 | Open |  
  
  
## 12.3.27 Compas direction  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the compass direction sensor.  | 3 | Open |  
  
  
## 12.3.28 Gyroscope data   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect information from the gyroscope data sensor.  | 3 | Open |  
  
  
## 12.3.29 Motor monitoring   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect and report all motor information | 1 | Open |  
  
