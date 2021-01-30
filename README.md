# german-industries-as-json
A list of German industries (de+en) generated using python from [official sources](https://www.destatis.de/DE/Methoden/Klassifikationen/Gueter-Wirtschaftsklassifikationen/klassifikation-wz-2008.html) by the Federal Office of Statistics. *This project is a private project. It's not affiliated to any government instances.*
  
:de:  
  
Eine Liste der Industrie-Bezeichnungen in Deutschland. Generiert mit einem Python Skript 
aus [Daten Statistischen Bundesamtes](https://www.destatis.de/DE/Methoden/Klassifikationen/Gueter-Wirtschaftsklassifikationen/klassifikation-wz-2008.html). Es handelt sich hierbei um ein privates Projekt, ohne
Verbindung zu offiziellen Stellen.

## JSON structure
```
{
    "A": 
    {
        "DE": "Land- und Forstwirtschaft, Fischerei",
        "EN": "Agriculture, forestry and fishing"
    },
    "B": 
    {
     "DE": "Bergbau und Gewinnung von Steinen und Erden", 
     "EN": "Mining and quarrying"
    },
    ...
}
```

## Data source and license
The data used is © [Statistisches Bundesamt, Wiesbaden 2008](https://www.klassifikationsserver.de/klassService/jsp/common/url.jsf?variant=wz2008)

Please refer to [this page](https://www.klassifikationsserver.de/klassService/jsp/common/url.jsf?variant=wz2008) for details about the source and data ownership. Distribution is permitted as long as the source is disclosed.
Additional information is available on the [destatis homepage](https://www.destatis.de/DE/Methoden/Klassifikationen/Gueter-Wirtschaftsklassifikationen/klassifikation-wz-2008.html).
  
Source file: https://www.klassifikationsserver.de/klassService/jsp/variant/downloadexport?type=EXPORT_XML_GROUPING&variant=wz2008&language=DE

I assume no responsibility for the correctness and completeness of the information provided as well as unauthorized modification of the information by third parties.

You can get in touch with me via vagrant-angora@maskmail.net

