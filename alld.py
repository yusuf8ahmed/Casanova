import pycountry
from ip2geotools.databases.noncommercial import DbIpCity
import pycountry_convert as pc
import requests
import netaddr
from datetime import datetime

"""
  ? ipel or ip-simple
  ? this libary uses an ipv4 address to get valuable info and doesnt use outdated databases or expensive api keys.
  ? Return all info in a dic
"""
class ipgeo: 
    def ip_all(ip):
        """
        This is only 95% percent accurate as
        as some value can change on a frequent basis

        And North Korea doesnt work
        """
        start_time = datetime.now()
        response = DbIpCity.get(ip, api_key='free')
        country = pycountry.countries.get(alpha_2=response.country)
        name = str(country.alpha_3).lower()

        url = "https://restcountries.eu/rest/v2/alpha/%s" % name
        url3 = "http://ip-api.com/json/%s?fields=mobile,proxy" % ip
        url4 = "https://api.iptoasn.com/v1/as/ip/%s" % ip
        url5 =  "https://worldtimeapi.org/api/ip/%s" % ip

        res = requests.get(url)
        res3 = requests.get(url3)
        res4 = requests.get(url4)
        res5 = requests.get(url5)

        con = res.json()
        con3 = res.json()
        con4 = res4.json()
        con5 = res5.json()

        
        if netaddr.valid_ipv4(ip) is True:
            ipv = "ipv4"
        if netaddr.valid_ipv6(ip) is True:
            ipv = "ipv6"

        finish_time = datetime.now()

        time = str(finish_time - start_time)

        ipf_a = {
                'ip': ip ,
                "type": ipv,
                'country_name': con["name"],
                'region_name': response.region,
                'city': response.city,
                'latitude': response.latitude,
                'longitude': response.longitude ,
                "location": {
                    'capital': con["capital"],
                    'Continent': con["region"],
                    "languages": con["languages"],
                    "broders": con["borders"],
                    "country_flag": "http://assets.ipstack.com/flags/%s.svg" % country.alpha_2.lower(),
                    "calling_code": con["callingCodes"],
                    "Main_Union": {
                                    "acronym": con["regionalBlocs"][0]['acronym'],
                                    "name":con["regionalBlocs"][0]['name']
                                    },
                    "Assoicated_Unions": len(con["regionalBlocs"])
                    },
                'time_zone': {
                        "id": con5["timezone"],
                        "current_time": con5["utc_datetime"],
                        "gmt_offset": con5["raw_offset"],
                        "code": con5["abbreviation"],
                        "is_daylight_saving": con5["dst"],
                        "unixtime": con5["unixtime"]
                    },
                'currency': con["currencies"],
                "connection": {
                            "mobile": con3["mobile"],
                            "proxy":con3["proxy"],
                            "asn":con4["as_number"],
                            "isp": con4["as_description"],
                            "Frist_ip": con4["first_ip"],
                            "Last_ip":con4["last_ip"]
                            },
                "time": {
                        "response time": time,
                        "acceptable time": " under 3s"

                        },
                }
        return ipf_a
            


