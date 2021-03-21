# Specification for User Interface Subsystem  

### Table of Contents  
  * [Specification for User Interface Subsystem](#specification-for-user-interface-subsystem)
    * [7.7 Speed Information](#77-speed-information)
    * [7.8 Turning Signal Information](#78-turning-signal-information)
    * [7.9 Hazard Light Information](#79-hazard-light-information)
    * [7.10 Energy Storage Warning Information](#710-energy-storage-warning-information)
    * [7.11 Instrumentation Power Supply](#711-instrumentation-power-supply)
    * [12.4.1.1 Left/right indicator ](#12411-leftright-indicator-)
    * [12.4.1.2 Battery warning data](#12412-battery-warning-data)
    * [12.4.1.3 Hazard lights](#12413-hazard-lights)
    * [12.4.1.4 Speed data](#12414-speed-data)
    * [12.4.1.5 Road position](#12415-road-position)
    * [12.4.1.6 Race strategy speed](#12416-race-strategy-speed)
    * [12.4.1.7 Road position](#12417-road-position)
    * [12.4.1.8 Display size](#12418-display-size)
    * [12.4.1.9 Readability at a distance ](#12419-readability-at-a-distance-)
    * [12.4.1.10 Direct sunlight ](#124110-direct-sunlight-)
    * [12.4.2.1 Location](#12421-location)
    * [12.4.2.2 Route](#12422-route)
    * [12.4.2.3 Collect data - speed](#12423-collect-data---speed)
    * [12.4.2.4 Collect data - tyre pressure](#12424-collect-data---tyre-pressure)
    * [12.4.2.5 Collect data - temp in cabin](#12425-collect-data---temp-in-cabin)
    * [12.4.2.6 Collect data - motor temp](#12426-collect-data---motor-temp)
    * [12.4.2.7 Collect data - battery voltage](#12427-collect-data---battery-voltage)
    * [12.4.2.8 Collect data - battery level](#12428-collect-data---battery-level)
    * [12.4.2.9 Multimedia volume ](#12429-multimedia-volume-)
    * [12.4.2.10 Multimedia](#124210-multimedia)
    * [12.4.2.11 Race strategy info](#124211-race-strategy-info)
    * [12.4.2.12 Readability at a distance](#124212-readability-at-a-distance)
    * [12.4.2.13 Display size ](#124213-display-size-)
    * [12.4.2.14 Dust proof ](#124214-dust-proof-)
    * [12.4.2.15 Vibration resistance ](#124215-vibration-resistance-)
    * [12.4.2.16 Operating voltage ](#124216-operating-voltage-)

## 7.7 Speed Information  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| The speed of the vehicle must always be displayed to the driver while they are driving | IMP |  |  
  
  
## 7.8 Turning Signal Information  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Turning signal information, i.e. whether it is on or off, must be displayed to the driver while they are driving | IMP |  |  
  
  
## 7.9 Hazard Light Information  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Hazard light information, i.e. whether they are on or off, must be displayed to the driver while they are driving. | IMP |  |  
  
  
## 7.10 Energy Storage Warning Information  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| All battery system warnings should be displayed to the driver when they are driving. | IMP |  |  
  
  
## 7.11 Instrumentation Power Supply  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| All in-car displays and other interior instrumentation should be powered by the main power storage, not external batteries or chargers. | IMP |  |  
  
  
## 12.4.1.1 Left/right indicator   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect the left/right indicator input from the embedded systems.  | 1 | Open |  
  
  
## 12.4.1.2 Battery warning data  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect the battery warning data from the embedded systems.  | 1 | Open |  
  
  
## 12.4.1.3 Hazard lights  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect the hazard lights input from the embedded systems.  | 1 | Open |  
  
  
## 12.4.1.4 Speed data  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect the speed data from the embedded systems.  | 1 | Open |  
  
  
## 12.4.1.5 Road position  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Collect the road position from the embedded systems.  | 1 | Open |  
  
  
## 12.4.1.6 Race strategy speed  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display suggested race strategy speed as a secondary speed   | 1 | Open |  
  
  
## 12.4.1.7 Road position  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display suggested road position  | 1 | Open |  
  
  
## 12.4.1.8 Display size  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| The display must be 4-6 inches diagonally   | 2 | Open |  
  
  
## 12.4.1.9 Readability at a distance   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| All information must be readable at 50cm away   | 1 | Open |  
  
  
## 12.4.1.10 Direct sunlight   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Information must be readable in direct sunlight  | 1 | Open |  
  
  
## 12.4.2.1 Location  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display the solar cars location. | 2 | Open |  
  
  
## 12.4.2.2 Route  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Determine the route given a starting and ending position | 2 | Open |  
  
  
## 12.4.2.3 Collect data - speed  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display speed collected from the embedded systems. | 1 | Open |  
  
  
## 12.4.2.4 Collect data - tyre pressure  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display tyre pressure collected from the embedded systems. | 1 | Open |  
  
  
## 12.4.2.5 Collect data - temp in cabin  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display temperature inside the cabin collected from the embedded systems. | 1 | Open |  
  
  
## 12.4.2.6 Collect data - motor temp  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display motor temperature collected from the embedded systems. | 1 | Open |  
  
  
## 12.4.2.7 Collect data - battery voltage  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display battery voltage collected from the embedded systems. | 1 | Open |  
  
  
## 12.4.2.8 Collect data - battery level  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display battery level collected from the embedded systems. | 1 | Open |  
  
  
## 12.4.2.9 Multimedia volume   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control the volume of music inside the cabin  | 1 | Open |  
  
  
## 12.4.2.10 Multimedia  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Control multimedia  | 2 | Open |  
  
  
## 12.4.2.11 Race strategy info  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| Display race strategy information   | 1 | Open |  
  
  
## 12.4.2.12 Readability at a distance  
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| All information must be readable from 1m away   | 1 | Open |  
  
  
## 12.4.2.13 Display size   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| The display must be 15 inches diagonal (+- 1 inch)  | 1 | Open |  
  
  
## 12.4.2.14 Dust proof   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| The display must be dust proof   | 1 | Open |  
  
  
## 12.4.2.15 Vibration resistance   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| The display must be vibration resistant   | 1 | Open |  
  
  
## 12.4.2.16 Operating voltage   
  
| Description | Priority | Verification Status |  
|:---:|:---:|:---:|  
| The display must operate at 12V  | 1 | Open |  
  
