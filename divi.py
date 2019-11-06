import pycountry
from ip2geotools.databases.noncommercial import DbIpCity
import pycountry_convert as pc
import requests
from datetime import datetime
from platform import mac_ver, win32_ver, linux_distribution, system
from sys import version_info as vi
import distro

class ipgeo:
        def location(ip):
                """
                Location returns a python dictonary with the following keys                        
                        'ip': ,
                        "type": ,
                        'country_name': ,
                        'region_name': ,
                        'city': ,
                        'latitude': ,
                        'longitude': ,
                        "location": {
                                'capital': ,
                                'Continent': ,
                                "languages": ,
                                "broders": ,
                                "country_flag":,
                                "calling_code":,
                                        "Main_Union": {
                                        "acronym": ,
                                        "name":
                                },
                                "Assoicated_Unions": ,
                                },
                        "time": {
                        "response time": time,
                        "acceptable time": " under 3s"
                        

                """
                start_time = datetime.now()
                response = DbIpCity.get(ip, api_key='free')
                country = pycountry.countries.get(alpha_2=response.country)
                name = str(country.alpha_3).lower()

                url = "https://restcountries.eu/rest/v2/alpha/%s" % name
                res = requests.get(url)
                con = res.json()

                finish_time = datetime.now()
                time = str(finish_time - start_time)
                loca = {
                        'ip': ip ,
                        "type": "ipv4",
                        'country_name': con["name"],
                        'region_name': response.region,
                        'city': response.city,
                        'latitude': response.latitude,
                        'longitude': response.longitude,
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
								"Assoicated_Unions": len(con["regionalBlocs"]),
								},
                        "time": {
                        "response time": time,
                        "acceptable time": " under 3s"
                        }
                        }
                return loca

        def timezone(ip):  
                """
                'ip': ip ,
                "type": "ipv4",
                "id": con5["timezone"],
                "current_time": con5["utc_datetime"],
                "gmt_offset": con5["raw_offset"],
                "code": con5["abbreviation"],
                "is_daylight_saving": con5["dst"],
                "unixtime": con5["unixtime"]
                "time": {
                "response time": time,
                "acceptable time": " under 3s"
                }

                """
                start_time = datetime.now() 

                url5 =  "https://worldtimeapi.org/api/ip/%s" % ip
                res5 = requests.get(url5)
                con5 = res5.json()

                finish_time = datetime.now()
                time = str(finish_time - start_time)
                time_zone =  {
                        'ip': ip ,
                        "type": "ipv4",
                        "id": con5["timezone"],
                        "current_time": con5["utc_datetime"],
                        "gmt_offset": con5["raw_offset"],
                        "code": con5["abbreviation"],
                        "is_daylight_saving": con5["dst"],
                        "unixtime": con5["unixtime"],
                        "time": {
                                "response time": time,
                                "acceptable time": " under 3s"
                }
                }
                return time_zone

        def currency(ip):
                """
                currency: [{
                'code': 'CAD',
                'name': 'Canadian dollar',
                'symbol': '$'
                }]
                """

                response = DbIpCity.get(ip, api_key='free')
                country = pycountry.countries.get(alpha_2=response.country)
                name = str(country.alpha_3).lower()

                start_time = datetime.now() 

                url = "https://restcountries.eu/rest/v2/alpha/%s" % name
                res = requests.get(url)
                con = res.json()

                finish_time = datetime.now()

                time = str(finish_time - start_time)
                money = {
                "currency" : con["currencies"],
                        "time": {
                        "response time": "time",
                        "acceptable time": " under 3s"
                } 
                }
                return money

        def connection(ip):
                """
                "connection": {
                "mobile": con3["mobile"],
                "proxy":con3["proxy"],
                "asn":con4["as_number"],
                "isp": con4["as_description"],
                "Frist_ip": con4["first_ip"],
                "Last_ip":con4["last_ip"]
                },
                """

                start_time = datetime.now() 

                url3 = "http://ip-api.com/json/%s?fields=mobile,proxy" % ip
                url4 = "https://api.iptoasn.com/v1/as/ip/%s" % ip

                res3 = requests.get(url3)
                res4 = requests.get(url4)

                con3 = res3.json()
                con4 = res4.json()

                finish_time = datetime.now()

                time = str(finish_time - start_time)

                conn =  {
                "mobile": con3["mobile"],
                "proxy":con3["proxy"],
                "asn":con4["as_number"],
                "isp": con4["as_description"],
                "Frist_ip": con4["first_ip"],
                "Last_ip":con4["last_ip"],
                        "time": {
                        "response time": "time",
                        "acceptable time": " under 3s"
                }
                },
                return conn

        def your_ip():
                """
                "yourip" =  {
                "Your_ip": res,
                },

                """

                start_time = datetime.now() 

                __version__ = '1.0.0'

                OS_VERSION_INFO = {
                'Linux': '%s' % (distro.linux_distribution()[0]),
                'Windows': '%s' % (win32_ver()[0]),
                'Darwin': '%s' % (mac_ver()[0]),
                }

                USER_AGENT = 'python-ipify/%s python/%s %s/%s' % (
                __version__,
                '%s.%s.%s' % (vi.major, vi.minor, vi.micro),
                system(),
                OS_VERSION_INFO.get(system(), ''),
                )

                res = requests.get("https://api.ipify.org", headers={'user-agent': "USER_AGENT"})

                finish_time = datetime.now()
                time = str(finish_time - start_time)

                yourip =  {
                "Your_ip": res.text,
                        "time": {
                        "response time": "time",
                        "acceptable time": " under 3s"
                } 
                },
                return yourip

