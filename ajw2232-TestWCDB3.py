# -*- coding: utf-8 -*-
"""
Created on Thu Apr 04 22:11:29 2013

@author: TechKnuckle Support
"""

import StringIO
import unittest
import _mysql

from WCDB4 import *

class TestWCDB2 (unittest.TestCase) :
    #----
    # login
    #----
    
    def test_login_1 (self) :
        c = _mysql.connect(
            host = "z",
            user = "coe78",
            passwd = "Oxt3emCwAR",
            db = "cs327e_coe78")
        self.assert_(str(type(c)) == "<type '_mysql.connection'>")
    
    
    def test_login_2 (self) :
        c = _mysql.connect(
            host = "z",
            user = "jstevens",
            passwd = "1JdQHwNNzr",
            db = "cs327e_jstevens")
        self.assert_(str(type(c)) == "<type '_mysql.connection'>")
        
    def test_login_3 (self) :
        c = login()
        self.assert_(str(type(c)) == "<type '_mysql.connection'>")


    #------
    # query
    #------
    
    def test_query_1 (self) :
        c = login()
        t = query(c, "DROP TABLE IF EXISTS Test1;")
        x = query(c, """
            create table Test1(
                name text);
            """)
        fill_tables('Test1', [{'name': "Sally"}, {'name': "Tom"}], c)
        t = query(c, "SELECT name FROM Test1;")
        self.assert_(t) == (('Sally',),('Tom',),)

    def test_query_2 (self) :
        c = login()
        t = query(c, "DROP TABLE IF EXISTS Test2;")
        x = query(c, """
            create table Test2(
                animal text,
                sound  text);
            """)
        fill_tables('Test2', [{'animal': "horse", 'sound': "neigh"}, {'sound': "quack", 'animal': "duck"}], c)
        t = query( c, "SELECT animal, sound FROM Test2")
        self.assert_(t) == (('horse', 'neigh',),('duck', 'quack',),)

    def test_query_3 (self) :
        c = login()
        t = query(c, "DROP TABLE IF EXISTS Test3;")
        x = query(c, """
            create table Test3(
                furniture  text,
                color      text,
                usefulness int);
            """)
        fill_tables('Test3', [{'furniture': "table", 'color': "white", 'usefulness': '8'} ,\
                              {'color': "purple", 'usefulness': '9', 'furniture': "couch"},\
                              {'usefulness': '1', 'furniture': "vase", 'color': "blue"}], c)
        t = query( c, "SELECT furniture, color, usefulness FROM Test3")
        self.assert_(t)== (('table', 'white', '8',),('couch', 'purple', '9',),('vase', 'blue', '1',),)    


    # ----
    # read
    # ----
    
    def test_read_1 (self):
        r = StringIO.StringIO("Test String")
        a = [""]
        p= WCDB_read(r, a)
        self.assert_(a[0] == "Test String")
        self.assert_(p == True)

    def test_read_2 (self):
        r = StringIO.StringIO("Test String\n Second Line")
        a = [""]
        p= WCDB_read(r, a)
        self.assert_(p == True)
        self.assert_(a[0] == "Test String\n")

    def test_read_3 (self):
        r = StringIO.StringIO("")
        a = [""]
        p= WCDB_read(r, a)
        self.assert_(p == False)
        self.assert_(a[0] == "")




    #------------
    # fill_tables
    #------------
    def test_fill_tables1 (self):
        c = login()
        x = query(c, "DROP TABLE IF EXISTS Test;")
        t = query(c, """
            create table Test(
                name text,
                age  int);
            """)
        info = [{'name': "Joseph Stevens", 'age': '12'}, {'name': "Annie Wu", 'age':'14'}]
        fill_tables('Test', info, c)
        sel = query(c, "SELECT name, age FROM Test")
        self.assert_(sel) == (('Joseph Stevens', '12'),('Annie Wu', '14'),)
        

    def test_fill_tables2 (self):
        c = login()
        x = query(c, "DROP TABLE IF EXISTS Test;")
        t = query(c, """
            create table Test(
                name text,
                age  int);
            """)
        info = [{'name': "Joseph Stevens", 'age': '12'}, {'name': "Annie Wu", 'age':'14'}, {'age':'100', 'name':"Isaiah"}]
        fill_tables('Test', info, c)
        sel = query(c, "SELECT name, age FROM Test")
        self.assert_(sel) == (('Joseph Stevens', '12',),('Annie Wu', '14',),('Isaiah', '100',),)
        
    def test_fill_tables3 (self):
        c = login()
        x = query(c, "DROP TABLE IF EXISTS Test;")
        t = query(c, """
            create table Test(
                name text,
                age  int);
            """)
        info = [{'age': '12', 'name': "Joseph Stevens"}]
        fill_tables('Test', info, c)
        sel = query(c, "SELECT name, age FROM Test")
        self.assert_(sel) == (('Joseph Stevens', '12',),)
        


    #-------------
    # create_table
    #-------------
    def test_create_table1 (self):
        c = create_table()
        t = query(c, "SHOW TABLES like 'Crisis';")
        self.assert_(t) == (('Crisis',),)
        
    def test_create_table2 (self):
        c = create_table()
        t = query(c, "SHOW TABLES like 'Organization';")
        self.assert_(t) != (('Persons',),)

    def test_create_table3 (self):
        c = create_table()
        t = query(c, "SHOW TABLES like 'HelloWorld';")
        self.assert_(str(t)) == "()"
        



##    #----------------------
##    # generate_dictionaries
##    #----------------------                                                            
                                             
import unittest
import xml.etree.cElementTree as et
from WCDB2 import generate_dictionaries

xml_file = """
    <WorldCrises>
      <Crisis crisisIdent = "E2001">
        <Name> Syrian Civil War </Name>
        <Kind crisisKindIdent="FC" />
        <Location>
          <Locality> Houston </Locality>
          <Region> TX </Region>
          <Country> United States </Country>
        </Location>
        <StartDateTime>
          <Date> 2001-08-14 </Date>
        </StartDateTime>
        <HumanImpact>
          <Type> Financial Loss </Type>
          <Number> 60000000000 </Number>
        </HumanImpact>
        <EconomicImpact> Greatest stock value loss in peaceful times and the largest bankruptcy in American history. </EconomicImpact>
        <ExternalResources>
          <ImageURL>http://rememberinghistory.files.wordpress.com/2012/11/enron_logo.jpg%3Fw%3D610 </ImageURL>
          <VideoURL>http://www.youtube.com/watch?v=QS5aosxUfvY</VideoURL>
          <MapURL>https://maps.google.com/maps?hl=enampq=1400+smith+street+houston+77002ampbav=on.2,or.r_gc.r_pw.r_cp.r_qf.ampbvm=bv.43287494,d.b2Iampbiw=640ampbih=679ampum=1ampie=UTF-8ampsa=Namptab=wl </MapURL>
        </ExternalResources>
        <RelatedPersons>
          <RelatedPerson personIdent="KLay" />
          <RelatedPerson personIdent="AGreenspan" />
        </RelatedPersons>
        <RelatedOrganizations>
          <RelatedOrganization organizationIdent = "SEC" />
        </RelatedOrganizations>
      </Crisis>

      <Organization organizationIdent="USDA">
        <Name>United States Department of Agriculture</Name>
        <Kind organizationKindIdent="AD"/>
        <Location>
          <Locality>Washington</Locality>
          <Region>D.C.</Region>
          <Country>United States</Country>
        </Location>
        <History>On May 15, 1862, Abraham Lincoln signed into law the Agricultural Act that established the U.S. Department of Agriculture. Since then, the Department has had a rich and varied history. The resources below explore that history, along with the history and organization of USDA's associated agencies and staff offices.</History>
        <ContactInfo>
          <Telephone>202 720 2791</Telephone>
          <Fax></Fax>
          <Email></Email>
          <PostalAddress>
            <StreetAddress>1400 Independence Ave., S.W.</StreetAddress>
            <Locality>Washington</Locality>
            <Region>D.C.</Region>
            <PostalCode>20250</PostalCode>
            <Country>United States</Country>
          </PostalAddress>
        </ContactInfo>
        <ExternalResources>
          <ImageURL>https://www.google.com/search?hl=enamprlz=1C2DVCR_enUS407US456ampq=USDA+imagesampbav=on.2,or.r_gc.r_pw.r_qf.ampbvm=bv.43287494,d.b2Iampbiw=1241ampbih=584ampum=1ampie=UTF-8amptbm=ischampsource=ogampsa=Namptab=wiampei=w_M3UfOvN4rA2AXRtoDYBQ#imgrc=3587T5k4YZYdfM%3A%3BDip-rsLNM2aALM%3Bhttp%253A%252F%252Fionenewsone.files.wordpress.com%252F2011%252F05%252Fusda_logo_rev.gif%3Bhttp%253A%252F%252Fnewsone.com%252F1227425%252Fusda-civil-rights-shirley-sherrod%252F%3B1233%3B850; </ImageURL>
          <VideoURL>http://video.foxbusiness.com/v/2174388754001/usda-under-fire-for-controversial-cultural-sensitivity-training/; </VideoURL>
          <MapURL>https://maps.google.com/maps?hl=enampq=1400+Independence+Ave.,+S.W.ampie=UTF-8amphq=amphnear=0x89b7b79fa4334315:0xfb36514e8557abaf,1400+Independence+Ave+SW,+Washington,+DC+20024ampgl=usampei=ePY3UeLYCqOU2wWR4IGoCgampved=0CDMQ8gEwAQ; </MapURL>
          <SocialNetworkURL>http://www.facebook.com/pages/USDA/106119542761892?fref=ts</SocialNetworkURL>
        </ExternalResources>
        <RelatedCrises>
          <RelatedCrisis crisisIdent="CE1970"></RelatedCrisis>
        </RelatedCrises>
        <RelatedPersons>
          <RelatedPerson personIdent="GWBush"></RelatedPerson>
          <RelatedPerson personIdent="BHObama"></RelatedPerson>
          <RelatedPerson personIdent="CHardin"></RelatedPerson>
        </RelatedPersons>
      </Organization>

      <Person personIdent="FDRoosevelt">
        <Name>
          <FirstName>Franklin</FirstName>
          <MiddleName>Delano</MiddleName>
          <LastName>Roosevelt</LastName>
          <Suffix></Suffix>
        </Name>
        <Kind personKindIdent="PR"/>
        <Location>
          <Locality>Hyde Park</Locality>
          <Region>New York</Region>
          <Country>United States</Country>
        </Location>
        <ExternalResources>
          <ImageURL>http://media.npr.org/assets/img/2012/12/18/ap07021209188_wide-5c891c581ba4583ae9dd3c2f9e16e95121c37d12-s6-c10.jpg </ImageURL>
          <VideoURL>http://www.history.com/topics/franklin-d-roosevelt/videos#fdr-a-voice-of-hope </VideoURL>
        </ExternalResources>
        <RelatedCrises>
          <RelatedCrisis crisisIdent="GD1929"></RelatedCrisis>
          <RelatedCrisis crisisIdent="WWII1939"></RelatedCrisis>
        </RelatedCrises>
        <RelatedOrganizations>
          <RelatedOrganization organizationIdent="FDIC"></RelatedOrganization>
          <RelatedOrganization organizationIdent="FR"></RelatedOrganization>
        </RelatedOrganizations>
      </Person>



      <CrisisKind crisisKindIdent = "EC">
        <Name> Economic Crisis </Name>
        <Description> Crisis that significantly alters and threatens the economic state of the region. </Description>
      </CrisisKind>

      <CrisisKind crisisKindIdent = "FC">
        <Name> Financial Crisis </Name>
        <Description> Crisis that results in a significant loss of money. </Description>
      </CrisisKind>

      <CrisisKind crisisKindIdent = "MC">
        <Name> Military Crisis </Name>
        <Description> Crisis that requires military involvement, often war. </Description>
      </CrisisKind>

      <CrisisKind crisisKindIdent = "E">
        <Name> Epidemic </Name>
        <Description> Crisis that results in widespread disease and sickness. </Description>
      </CrisisKind>


      <OrganizationKind organizationKindIdent="AD">
        <Name>Agricultural Department</Name>
        <Description>Responsible for developing and executing U.S. federal government policy on farming, agriculture, forestry, and food.</Description>
      </OrganizationKind>

      <OrganizationKind organizationKindIdent="NS">
        <Name>National Security</Name>
        <Description>Maintain the survival of the state through the use of economic power, diplomacy, power projection and political power.</Description>
      </OrganizationKind>

      <OrganizationKind organizationKindIdent="IC">
        <Name>Insurance Corporation</Name>
        <Description>It provides deposit insurance guaranteeing the safety of a depositor's accounts.</Description>
      </OrganizationKind>

      <OrganizationKind organizationKindIdent="CB">
        <Name>Central Bank</Name>
        <Description>Is a public institution that manages a state's currency, money supply, and interest rates. Central banks also usually oversee the commercial banking system of their respective countries.</Description>
      </OrganizationKind>

      <OrganizationKind organizationKindIdent="MA">
        <Name>Military Alliance</Name>
        <Description>A security arrangement, regional or global, in which each state in the system accepts that the security of one is the concern of all, and agrees to join in a collective response to threats to, and breaches of, the peace.</Description>
      </OrganizationKind>

      <OrganizationKind organizationKindIdent="IB">
        <Name>Investment Bank</Name>
        <Description>Is a financial institution that assists individuals, corporations, and governments in raising capital by underwriting and/or acting as the client's agent in the issuance of securities.</Description>
      </OrganizationKind>

      <OrganizationKind organizationKindIdent="TO">
        <Name>Terrorist Organization</Name>
        <Description>A political movement that uses terror as a weapon to achieve its goals.</Description>
      </OrganizationKind>

      <PersonKind personKindIdent="PR">
        <Name>President</Name>
        <Description>Is a leader of an organization, company, community, club, trade union, university, country, a division or part of any of these, or, more generally, anything else.</Description>
      </PersonKind>

      <PersonKind personKindIdent="TL">
        <Name>Terrorist Leader</Name>
        <Description>A leader of a group who uses or advocates terrorism.</Description>
      </PersonKind>

      <PersonKind personKindIdent="FRC">
        <Name>Federal Reserve Chairman</Name>
        <Description>Is the head of the central banking system of the United States.</Description>
      </PersonKind>

      <PersonKind personKindIdent="BM">
        <Name>Businessman</Name>
        <Description>Is someone involved in a particular undertaking of activities, commercial or industrial, for the purpose of generating revenue from a combination of human, financial, and physical capital.</Description>
      </PersonKind>

      <PersonKind personKindIdent="SA">
        <Name>Secretary of Agriculture</Name>
        <Description>Is the head of the United States Department of Agriculture.</Description>
      </PersonKind>

    </WorldCrises>
            """


xml_file2="""

    <WorldCrises>
      <Crisis crisisIdent = "c2">
       <Name>name2</Name>
       <Kind crisisKindIdent = "ck2" />
       <Location>
         <Locality>locality2</Locality>
         <Region>region2</Region>
         <Country>country2</Country>
       </Location>
       <StartDateTime>
         <Date>2222-02-02</Date>

       </StartDateTime>
       <HumanImpact>
         <Type>type2</Type>
         <Number>2222222222</Number>
       </HumanImpact>
       <EconomicImpact>economicimpact2</EconomicImpact>
       <ExternalResources>
         <ImageURL>http://22.com</ImageURL>
         <VideoURL>http://www.222.com</VideoURL>
         <MapURL>https://www.222222.org</MapURL>
       </ExternalResources>
       <RelatedPersons>
         <RelatedPerson personIdent = "p2" />
       </RelatedPersons>
       <RelatedOrganizations>
        <RelatedOrganization organizationIdent = "o2" />
       </RelatedOrganizations>
      </Crisis>

      <Organization organizationIdent="o2">
        <Name>name2</Name>
        <Kind organizationKindIdent="ok2"/>
        <Location>
          <Locality>locality2</Locality>
          <Region>region2</Region>
          <Country>country2</Country>
        </Location>
        <History>history2</History>
        <ContactInfo>
          <Telephone/>
          <Fax/>
          <Email/>
          <PostalAddress>
            <StreetAddress/>
            <Locality>locality2</Locality>
            <Region>region2</Region>
            <PostalCode>22222</PostalCode>
            <Country>country2</Country>
          </PostalAddress>
        </ContactInfo>
        <ExternalResources>
          <ImageURL>https://22.2222.edu</ImageURL>
        </ExternalResources>
        <RelatedCrises>
          <RelatedCrisis crisisIdent="c2"></RelatedCrisis>
        </RelatedCrises>
        <RelatedPersons>
          <RelatedPerson personIdent="p2"></RelatedPerson>
        </RelatedPersons>
      </Organization>

      <Person personIdent="p2">
        <Name>
          <FirstName>firstname2</FirstName>
          <MiddleName>middlename2</MiddleName>
          <LastName>lastname2</LastName>
        </Name>
        <Kind personKindIdent="pk2"/>
        <Location>
          <Locality>locality2</Locality>
          <Region>region2</Region>
          <Country>unitedstates2</Country>
        </Location>
        <ExternalResources>
          <ImageURL>http://22.222.org/22/222/2/22/2/2222/22.jpg</ImageURL>
          <VideoURL>http://2.com</VideoURL>
        </ExternalResources>
        <RelatedCrises>
          <RelatedCrisis crisisIdent="c2"></RelatedCrisis>
        </RelatedCrises>
        <RelatedOrganizations>
          <RelatedOrganization organizationIdent="o2"></RelatedOrganization>
        </RelatedOrganizations>
    </Person>

      <CrisisKind crisisKindIdent = "ck2">
        <Name>crisis name 2</Name>
        <Description>crisiskindIdent for acceptance test 2</Description>
      </CrisisKind>

      <OrganizationKind organizationKindIdent="ok2">
        <Name>organization name 2</Name>
        <Description>organizationkindIdent for acceptance test 2</Description>
      </OrganizationKind>

      <PersonKind personKindIdent="pk2">
        <Name>person name 2</Name>
        <Description>personkindIdent for acceptance test 2</Description>
      </PersonKind>

    </WorldCrises>
"""

xml_file3="""

    <WorldCrises>
      <Crisis crisisIdent = "c2">
       <Name>name2</Name>
       <Kind crisisKindIdent = "ck2" />
       <Location>
         <Locality>locality2</Locality>
         <Region>region2</Region>
         <Country>country2</Country>
       </Location>
       <StartDateTime>
         <Date>2222-02-02</Date>

       </StartDateTime>
       <HumanImpact>
         <Type>type2</Type>
         <Number>2222222222</Number>
       </HumanImpact>
       <EconomicImpact>economicimpact2</EconomicImpact>
       <ExternalResources>
         <ImageURL>http://22.com</ImageURL>
         <VideoURL>http://www.222.com</VideoURL>
         <MapURL>https://www.222222.org</MapURL>
       </ExternalResources>
       <RelatedPersons>
         <RelatedPerson personIdent = "p2" />
       </RelatedPersons>
       <RelatedOrganizations>
        <RelatedOrganization organizationIdent = "o2" />
       </RelatedOrganizations>
      </Crisis>

      <Crisis crisisIdent = "c2">
       <Name>name2</Name>
       <Kind crisisKindIdent = "ck2" />
       <Location>
         <Locality>locality2</Locality>
         <Region>region2</Region>
         <Country>country2</Country>
       </Location>
       <StartDateTime>
         <Date>2222-02-02</Date>

       </StartDateTime>
       <HumanImpact>
         <Type>type2</Type>
         <Number>2222222222</Number>
       </HumanImpact>
       <EconomicImpact>economicimpact2</EconomicImpact>
       <ExternalResources>
         <ImageURL>http://22.com</ImageURL>
         <VideoURL>http://www.222.com</VideoURL>
         <MapURL>https://www.222222.org</MapURL>
       </ExternalResources>
       <RelatedPersons>
         <RelatedPerson personIdent = "p2" />
       </RelatedPersons>
       <RelatedOrganizations>
        <RelatedOrganization organizationIdent = "o2" />
       </RelatedOrganizations>
      </Crisis>
    </WorldCrises>

"""

xml_file4="""

    <WorldCrises>
      <Crisis crisisIdent = "c2">
       <Name>name2</Name>
       <Kind crisisKindIdent = "ck2" />
       <Location>
         <Locality>locality2</Locality>
         <Region>region2</Region>
         <Country>country2</Country>
       </Location>
       <StartDateTime>
         <Date>2222-02-02</Date>

       </StartDateTime>
       <HumanImpact>
         <Type>type2</Type>
         <Number>2222222222</Number>
       </HumanImpact>
       <EconomicImpact>economicimpact2</EconomicImpact>
       <ExternalResources>
         <ImageURL>http://22.com</ImageURL>
         <VideoURL>http://www.222.com</VideoURL>
         <MapURL>https://www.222222.org</MapURL>
       </ExternalResources>
       <RelatedPersons>
         <RelatedPerson personIdent = "p2" />
       </RelatedPersons>
       <RelatedOrganizations>
        <RelatedOrganization organizationIdent = "o2" />
       </RelatedOrganizations>
      </Crisis>
    </WorldCrises>

"""

xml_file5 = """
    <WorldCrises>
      <Crisis crisisIdent="Enron_EC_2001"><Name>Enron Collapse</Name><Kind crisisKindIdent="EC" /><Location><Locality>Houston</Locality><Region>TX</Region><Country>United States</Country></Location><StartDateTime><Date>2001-08-14</Date></StartDateTime><HumanImpact><Type>Financial Loss</Type><Number>60000000000</Number></HumanImpact><EconomicImpact>Greatest stock value loss in peaceful times and the largest bankruptcy in American history.</EconomicImpact><WaysToHelp /><ResourceNeeded /><ExternalResources><ImageURL>http://rememberinghistory.files.wordpress.com/2012/11/enron_logo.jpg%3Fw%3D610</ImageURL><VideoURL>http://www.youtube.com/watch?v=QS5aosxUfvY</VideoURL><MapURL>https://maps.google.com/maps?hl=enampq=1400+smith+street+houston+77002ampbav=on.2,or.r_gc.r_pw.r_cp.r_qf.ampbvm=bv.43287494,d.b2Iampbiw=640ampbih=679ampum=1ampie=UTF-8ampsa=Namptab=wl</MapURL></ExternalResources><RelatedPersons><RelatedPerson personIdent="KLay" /><RelatedPerson personIdent="AGreenspan" /></RelatedPersons><RelatedOrganizations><RelatedOrganization organizationIdent="SEC" /></RelatedOrganizations></Crisis><Crisis crisisIdent="Enron_EC_2001"><Name>Enron Collapse</Name><Kind crisisKindIdent="EC" /><Location><Locality>Houston</Locality><Region>TX</Region><Country>United States</Country></Location><StartDateTime><Date>2001-08-14</Date></StartDateTime><HumanImpact><Type /><Number /></HumanImpact><EconomicImpact /><WaysToHelp>Better Investing and pricing values</WaysToHelp><ResourceNeeded>Data on stocks and more exhaustive analysis</ResourceNeeded><ExternalResources><ImageURL>http://rememberinghistory.files.wordpress.com/2012/11/enron_logo.jpg%3Fw%3D610</ImageURL><VideoURL>http://www.youtube.com/watch?v=QS5aosxUfvY</VideoURL><MapURL>https://maps.google.com/maps?hl=enampq=1400+smith+street+houston+77002ampbav=on.2,or.r_gc.r_pw.r_cp.r_qf.ampbvm=bv.43287494,d.b2Iampbiw=640ampbih=679ampum=1ampie=UTF-8ampsa=Namptab=wl</MapURL></ExternalResources><RelatedPersons><RelatedPerson personIdent="KLay" /><RelatedPerson personIdent="AGreenspan" /></RelatedPersons><RelatedOrganizations><RelatedOrganization organizationIdent="SEC" /></RelatedOrganizations></Crisis>
 </WorldCrises>


""" 
    
xml_file6 = """
    <WorldCrises>
      <Crisis crisisIdent="Enron_EC_2001"><Name>Enron Collapse</Name><Kind crisisKindIdent="EC" /><Location><Locality>Houston</Locality><Region>TX</Region><Country>United States</Country></Location><StartDateTime><Date>2001-08-14</Date></StartDateTime><HumanImpact><Type>Financial Loss</Type><Number>60000000000</Number></HumanImpact><EconomicImpact>Greatest stock value loss in peaceful times and the largest bankruptcy in American history.</EconomicImpact><WaysToHelp>Better Investing and pricing values</WaysToHelp><ResourceNeeded>Data on stocks and more exhaustive analysis</ResourceNeeded><ExternalResources><ImageURL>http://rememberinghistory.files.wordpress.com/2012/11/enron_logo.jpg%3Fw%3D610</ImageURL><VideoURL>http://www.youtube.com/watch?v=QS5aosxUfvY</VideoURL><MapURL>https://maps.google.com/maps?hl=enampq=1400+smith+street+houston+77002ampbav=on.2,or.r_gc.r_pw.r_cp.r_qf.ampbvm=bv.43287494,d.b2Iampbiw=640ampbih=679ampum=1ampie=UTF-8ampsa=Namptab=wl</MapURL></ExternalResources><RelatedPersons><RelatedPerson personIdent="KLay" /><RelatedPerson personIdent="AGreenspan" /></RelatedPersons><RelatedOrganizations><RelatedOrganization organizationIdent="SEC" /></RelatedOrganizations></Crisis><Crisis crisisIdent="Enron_EC_2001"><Name>Enron Collapse</Name><Kind crisisKindIdent="EC" /><Location><Locality>Houston</Locality><Region>TX</Region><Country>United States</Country></Location><StartDateTime><Date>2001-08-14</Date></StartDateTime><HumanImpact><Type>Financial Loss</Type><Number>60000000000</Number></HumanImpact><EconomicImpact>Greatest stock value loss in peaceful times and the largest bankruptcy in American history.</EconomicImpact><WaysToHelp>Better Investing and pricing values</WaysToHelp><ResourceNeeded>Data on stocks and more exhaustive analysis</ResourceNeeded><ExternalResources><ImageURL>http://rememberinghistory.files.wordpress.com/2012/11/enron_logo.jpg%3Fw%3D610</ImageURL><VideoURL>http://www.youtube.com/watch?v=QS5aosxUfvY</VideoURL><MapURL>https://maps.google.com/maps?hl=enampq=1400+smith+street+houston+77002ampbav=on.2,or.r_gc.r_pw.r_cp.r_qf.ampbvm=bv.43287494,d.b2Iampbiw=640ampbih=679ampum=1ampie=UTF-8ampsa=Namptab=wl</MapURL></ExternalResources><RelatedPersons><RelatedPerson personIdent="KLay" /><RelatedPerson personIdent="AGreenspan" /></RelatedPersons><RelatedOrganizations><RelatedOrganization organizationIdent="SEC" /></RelatedOrganizations></Crisis>
 </WorldCrises>

"""

xml_file7 = """
    <WorldCrises>
      <Crisis crisisIdent="Enron_EC_2001"><Name>Enron Collapse</Name><Kind crisisKindIdent="EC" /><Location><Locality>Houston</Locality><Region>TX</Region><Country>United</Country></Location><StartDateTime><Date>2001-08-14</Date></StartDateTime><HumanImpact><Type>Financial Loss</Type><Number>60000000000</Number></HumanImpact><EconomicImpact>Greatest stock value loss in peaceful times and the largest bankruptcy in American history.</EconomicImpact><WaysToHelp>Better Investing and pricing values</WaysToHelp><ResourceNeeded>Data on stocks and more exhaustive analysis</ResourceNeeded><ExternalResources><ImageURL>http://rememberinghistory.files.wordpress.com/2012/11/enron_logo.jpg%3Fw%3D610</ImageURL><VideoURL>http://www.youtube.com/watch?v=QS5aosxUfvY</VideoURL><MapURL>https://maps.google.com/maps?hl=enampq=1400+smith+street+houston+77002ampbav=on.2,or.r_gc.r_pw.r_cp.r_qf.ampbvm=bv.43287494,d.b2Iampbiw=640ampbih=679ampum=1ampie=UTF-8ampsa=Namptab=wl</MapURL></ExternalResources><RelatedPersons><RelatedPerson personIdent="KLay" /><RelatedPerson personIdent="AGreenspan" /></RelatedPersons><RelatedOrganizations><RelatedOrganization organizationIdent="SEC" /></RelatedOrganizations></Crisis><Crisis crisisIdent="Enron_EC_2001"><Name>Enron Collapse</Name><Kind crisisKindIdent="EC" /><Location><Locality>Houston</Locality><Region>TX</Region><Country>United States</Country></Location><StartDateTime><Date>2001-08-14</Date></StartDateTime><HumanImpact><Type>Financial Loss</Type><Number>60000000000</Number></HumanImpact><EconomicImpact>Greatest stock value loss in peaceful times and the largest bankruptcy in American history.</EconomicImpact><WaysToHelp>Better Investing and pricing values</WaysToHelp><ResourceNeeded>Data on stocks and more exhaustive analysis</ResourceNeeded><ExternalResources><ImageURL>http://rememberinghistory.files.wordpress.com/2012/11/enron_logo.jpg%3Fw%3D610</ImageURL><VideoURL>http://www.youtube.com/watch?v=QS5aosxUfvY</VideoURL><MapURL>https://maps.google.com/maps?hl=enampq=1400+smith+street+houston+77002ampbav=on.2,or.r_gc.r_pw.r_cp.r_qf.ampbvm=bv.43287494,d.b2Iampbiw=640ampbih=679ampum=1ampie=UTF-8ampsa=Namptab=wl</MapURL></ExternalResources><RelatedPersons><RelatedPerson personIdent="KLay" /><RelatedPerson personIdent="AGreenspan" /></RelatedPersons><RelatedOrganizations><RelatedOrganization organizationIdent="SEC" /></RelatedOrganizations></Crisis>
 </WorldCrises>

"""
class MyTest(unittest.TestCase):

    def test_WCDB2_generater_dictionaries_1(self):
           root = et.fromstring(xml_file)
           crisis_list,location_list,organization_list, person_list, crisis_kind_list, person_kind_list, organization_kind_list = generate_dictionaries(root)
           x = crisis_list[0]
           self.assert_( x['start_date_time'] == ' 2001-08-14 ')

    def test_WCDB2_generater_dictionaries_2(self):
           root = et.fromstring(xml_file)
           crisis_list,location_list,organization_list, person_list, crisis_kind_list, person_kind_list, organization_kind_list = generate_dictionaries(root)
           x = organization_list[0]
           self.assert_( x['organizationIdent'] == 'USDA')

    def test_WCDB2_generater_dictionaries_3(self):
           root = et.fromstring(xml_file)
           crisis_list,location_list,organization_list, person_list, crisis_kind_list, person_kind_list, organization_kind_list = generate_dictionaries(root)
           x = location_list[0]
           self.assert_( x['country'] == ' United States ')


    #----------------------
    # WCDB2_print
    #----------------------

    
    def test_WCDB_print_1(self):
        w=StringIO.StringIO()
        root= et.fromstring(xml_file)
        r= WCDB_print(w,xml_file2)
        xml = et.tostring(root)
        self.assert_(r != xml)

    def test_WCDB_print_2(self):
        w=StringIO.StringIO()
        xml= xml_file
        r= WCDB_print(w,xml)
        self.assert_(r != xml)

    def test_WCDB_print_3(self):
        w=StringIO.StringIO()
        root= et.fromstring(xml_file2)
        xml = et.tostring(root)
        r = WCDB_print(w,xml)
        self.assert_(r == xml)

    def test_merge_1(self):
        root= et.fromstring(xml_file5)
        x= merge(root)
        y= et.fromstring(xml_file6)
        z=et.tostring(y)
        string = et.tostring(x)
        self.assert_(string == z)
        
    def test_merge_2(self):
        root= et.fromstring(xml_file3)
        x= merge(root)
        self.assert_(x != xml_file4)
        
    def test_merge_3(self):
        root= et.fromstring(xml_file5)
        x= merge(root)
        result = et.fromstring(xml_file7)
        
        self.assert_(et.tostring(x) != et.tostring(result))

##    def test_export_table(self):
##        element_list= [{'id':'E2001','name':'Syrian Civil War','economic_impact':'Greatest stock value loss in peaceful times and the largest bankruptcy in American history.'}]
##        c= create_table()
##        table_name= 'Crisis'
##        fill_tables(
##        xTable= export_table(c, table_name)
##        xml= et.tostring(xTable)
##
##        

if __name__=='__main__':
    print ("MyTest.py")
    unittest.main()
    print ('Done.')
    
