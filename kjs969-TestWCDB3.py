#!/usr/bin/env python

# ---------------------------
# Copyright (C) 2013
# Team: Better Late Than Never
# --------------------------

# -------
# imports
# -------

import xml.etree.ElementTree as ET
import os
import _mysql
import StringIO
import unittest
import sys

from WCDB3 import WCDB3_read, WCDB3_import, WCDB3_login, WCDB3_createTables, WCDB3_query, WCDB3_solve

# -----------
# TestWCDB3
# -----------

class TestWCDB3 (unittest.TestCase) :
    
    # -----------
    # WCDB3_read
    # -----------
    
    def test_read_1 (self):
        r = StringIO.StringIO("<country>\n<state></state>\n</country>")
        WCDB3_read(r)
        f = open("temp", 'r')
        lines = f.readlines()
        f.close()
        self.assert_(lines[0] == "<country>\n")
        self.assert_(lines[1] == "<state></state>\n")
        self.assert_(lines[2] == "</country>")

    
    def test_read_2 (self):
        r = StringIO.StringIO("<country></country>")
        WCDB3_read(r)
        f = open("temp", 'r')
        lines = f.readlines()
        f.close()
        self.assert_(lines[0] == "<country></country>")

    def test_read_3 (self):
        r = StringIO.StringIO("<a><b></b>\n<c><d>\n</d><e>\n</e></c></a>")
        WCDB3_read(r)
        f = open("temp", 'r')
        lines = f.readlines()
        f.close()
        self.assert_(lines[0] == "<a><b></b>\n")
        self.assert_(lines[1] == "<c><d>\n")
        self.assert_(lines[2] == "</d><e>\n")
        self.assert_(lines[3] == "</e></c></a>")


    # -----------
    # WCDB3_import
    # -----------
    
    def test_import_1 (self):
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        WCDB3_createTables(c)
        s = StringIO.StringIO("""<WorldCrises>
    <Crisis crisisIdent="TS_2004">
    </Crisis>
    <Organization organizationIdent="WNG">
    </Organization>
    <Person personIdent="JHickenlooper">
    </Person>
</WorldCrises>""")
        WCDB3_read(s)
        tree = ET.parse('temp')
        WCDB3_import(tree)
        t = WCDB3_query(c,"select * from Crisis;")
        self.assert_(t == (('TS_2004', '', '', '0000-00-00', None, None, None, ''),))

    def test_import_2 (self):
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        WCDB3_createTables(c)
        s = StringIO.StringIO("""<WorldCrises>
    <Crisis crisisIdent="CW2012">
    </Crisis>
    <Organization organizationIdent="WNG">
    </Organization>
    <Person personIdent="JHickenlooper">
    </Person>
</WorldCrises>""")
        WCDB3_read(s)
        tree = ET.parse('temp')
        WCDB3_import(tree)
        t = WCDB3_query(c,"select * from Organization;")
        self.assert_(t ==(('WNG', '', '', '', '', '', '', '', '', '', '', ''),))

    def test_import_3 (self):
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        WCDB3_createTables(c)
        s = StringIO.StringIO("""<WorldCrises>
    <Crisis crisisIdent="CW2012">
    </Crisis>
    <Organization organizationIdent="WNG">
    </Organization>
    <Person personIdent="JHickenlooper">
    </Person>
</WorldCrises>""")
        WCDB3_read(s)
        tree = ET.parse('temp')
        WCDB3_import(tree)
        t = WCDB3_query(c,"select * from Person;")
        self.assert_(t == (('JHickenlooper', '', None, '', None, ''),)
)
    c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
    WCDB3_query(c, "drop table if exists Crisis")
    WCDB3_query(c, "drop table if exists Organization")
    WCDB3_query(c, "drop table if exists Person")
    WCDB3_query(c, "drop table if exists Location")
    WCDB3_query(c, "drop table if exists HumanImpact")
    WCDB3_query(c, "drop table if exists ResourceNeeded")
    WCDB3_query(c, "drop table if exists WaysToHelp")
    WCDB3_query(c, "drop table if exists EconomicImpact")
    WCDB3_query(c, "drop table if exists ExternalResource")
    WCDB3_query(c, "drop table if exists CrisisOrganization")
    WCDB3_query(c, "drop table if exists OrganizationPerson")
    WCDB3_query(c, "drop table if exists PersonCrisis")
    WCDB3_query(c, "drop table if exists CrisisKind")

    # -----------
    # WCDB3_export
    # -----------
    
    def test_export_1 (self):
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        WCDB3_createTables(c)
        s = StringIO.StringIO("""<WorldCrises>
    <Crisis crisisIdent="TS_2004">
    </Crisis>
    <Organization organizationIdent="WNG">
    </Organization>
    <Person personIdent="JHickenlooper">
    </Person>
</WorldCrises>""")
        WCDB3_read(s)
        tree = ET.parse('temp')
        WCDB3_import(tree)
        t = WCDB3_query(c,"select * from Crisis;")
        self.assert_(t == (('TS_2004', '', '', '0000-00-00', None, None, None, ''),))

    def test_export_2 (self):
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        WCDB3_createTables(c)
        s = StringIO.StringIO("""<WorldCrises>
    <Crisis crisisIdent="CW2012">
    </Crisis>
    <Organization organizationIdent="WNG">
    </Organization>
    <Person personIdent="JHickenlooper">
    </Person>
</WorldCrises>""")
        WCDB3_read(s)
        tree = ET.parse('temp')
        WCDB3_import(tree)
        t = WCDB3_query(c,"select * from Organization;")
        self.assert_(t ==(('WNG', '', '', '', '', '', '', '', '', '', '', ''),))

    def test_export_3 (self):
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        WCDB3_createTables(c)
        s = StringIO.StringIO("""<WorldCrises>
    <Crisis crisisIdent="CW2012">
    </Crisis>
    <Organization organizationIdent="WNG">
    </Organization>
    <Person personIdent="JHickenlooper">
    </Person>
</WorldCrises>""")
        WCDB3_read(s)
        tree = ET.parse('temp')
        WCDB3_import(tree)
        t = WCDB3_query(c,"select * from Person;")
        self.assert_(t == (('JHickenlooper', '', None, '', None, ''),)
)
    c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
    WCDB3_query(c, "drop table if exists Crisis")
    WCDB3_query(c, "drop table if exists Organization")
    WCDB3_query(c, "drop table if exists Person")
    WCDB3_query(c, "drop table if exists Location")
    WCDB3_query(c, "drop table if exists HumanImpact")
    WCDB3_query(c, "drop table if exists ResourceNeeded")
    WCDB3_query(c, "drop table if exists WaysToHelp")
    WCDB3_query(c, "drop table if exists EconomicImpact")
    WCDB3_query(c, "drop table if exists ExternalResource")
    WCDB3_query(c, "drop table if exists CrisisOrganization")
    WCDB3_query(c, "drop table if exists OrganizationPerson")
    WCDB3_query(c, "drop table if exists PersonCrisis")
    WCDB3_query(c, "drop table if exists CrisisKind")
    
    # ------------
    # WCDB3_login
    # ------------

    def test_login_1 (self) :
        connection = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        assert str(type(connection)) == "<type '_mysql.connection'>"

    def test_login_2 (self) :
        connection = WCDB3_login("z", "kjs969", "+gW_J3pDyG", "cs327e_kjs969")
        assert str(type(connection)) == "<type '_mysql.connection'>"
        

    def test_login_3 (self) :
        connection = WCDB3_login("z", "bes749", "sng753!!", "cs327e_bes749")
        assert str(type(connection)) == "<type '_mysql.connection'>"

    # ------------
    # WCDB3_createTables
    # ------------

    
    def test_createTables_1 (self) :
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        WCDB3_createTables(c)
        t = WCDB3_query(c, "show COLUMNS from Crisis;")
        self.assert_( t == (('id', 'char(100)', 'NO', 'PRI', None, ''), ('name', 'text', 'NO', '', None, ''), ('kind', 'char(100)', 'NO', '', None, ''), ('start_date', 'date', 'NO', '', None, ''), ('start_time', 'time', 'YES', '', None, ''), ('end_date', 'date', 'YES', '', None, ''), ('end_time', 'time', 'YES', '', None, ''), ('economic_impact', 'char(100)', 'NO', '', None, '')))
    
    def test_createTables_2 (self) :
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        WCDB3_createTables(c)
        t = WCDB3_query(c, "show COLUMNS from HumanImpact;")
        self.assert_(t == (('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment'), ('crisis_id', 'char(100)', 'NO', '', None, ''), ('type', 'char(100)', 'NO', '', None, ''), ('number', 'int(11)', 'NO', '', None, '')))
 
    def test_createTables_3 (self) :
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        WCDB3_createTables(c)
        t = WCDB3_query(c, "show COLUMNS from WaysToHelp;")
        self.assert_( t == (('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment'), ('crisis_id', 'char(100)', 'NO', '', None, ''), ('description', 'text', 'YES', '', None, '')))

    c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
    WCDB3_query(c, "drop table if exists Crisis")
    WCDB3_query(c, "drop table if exists Organization")
    WCDB3_query(c, "drop table if exists Person")
    WCDB3_query(c, "drop table if exists Location")
    WCDB3_query(c, "drop table if exists HumanImpact")
    WCDB3_query(c, "drop table if exists ResourceNeeded")
    WCDB3_query(c, "drop table if exists WaysToHelp")
    WCDB3_query(c, "drop table if exists EconomicImpact")
    WCDB3_query(c, "drop table if exists ExternalResource")
    WCDB3_query(c, "drop table if exists CrisisOrganization")
    WCDB3_query(c, "drop table if exists OrganizationPerson")
    WCDB3_query(c, "drop table if exists PersonCrisis")
    WCDB3_query(c, "drop table if exists CrisisKind")
    
    # ------------
    # WCDB3_query
    # ------------
    
    WCDB3_createTables(c)
    
    def test_query_1 (self) :
        c = WCDB3_login("z", "dmoodz", "easy","cs327e_dmoodz")
        t = WCDB3_query(c, "select sqrt (3.67) from dual;") 
        self.assert_( t == (('1.9157244060668',),) )

    def test_query_2 (self) :
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        t = WCDB3_query( c, "select concat ('Michael', 'Jackson') as 'NAME' from dual;")
        self.assert_( t == (('MichaelJackson',),) )

    def test_query_3 (self) :
        c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
        t = WCDB3_query( c, "select power (2.512, 5) from dual")
        self.assert_( t == (('100.022608259449',),))    

    c = WCDB3_login("z", "dmoodz", "easy", "cs327e_dmoodz")
    WCDB3_query(c, "drop table if exists Crises")
    WCDB3_query(c, "drop table if exists Organizations")
    WCDB3_query(c, "drop table if exists Persons")
    WCDB3_query(c, "drop table if exists Relations")
    
    
    # -----------
    # WCDB3_solve
    # -----------

    def test_solve_1 (self) :
        r = StringIO.StringIO("""<?xml version="1.0" ?>
<WorldCrises>
    <Crisis crisisIdent="FL_1993">
            <Name>Great Flood of 1993</Name>
            <Kind crisisKindIdent="FL"></Kind>
            <Location>
                <Region>Mississippi, Louisiana, Iowa, Kansas, Minnesota, Missouri, Nebraska</Region>
                <Country>United States of America</Country>
            </Location>
            <StartDateTime>
                <Date>1993-04-01 </Date></StartDateTime>
            <EndDateTime><Date>1993-10-01</Date></EndDateTime>
        <HumanImpact><Type>Casualties</Type><Number> 50</Number></HumanImpact>
        <EconomicImpact>Damages: $15-20 billion</EconomicImpact>
        <ResourceNeeded>Sandbags; Army Corps of Engineers; Army National Guard; American Red Cross</ResourceNeeded>
        <WaysToHelp>Donation to American Red Cross</WaysToHelp>
        <ExternalResources>
            <ImageURL>http://mo.water.usgs.gov/Reports/1993-Flood/images/scan13.jpg</ImageURL>
            <VideoURL>http://www.youtube.com/watch?v=N5avsx-8xJo</VideoURL>
            <MapURL>http://earthobservatory.nasa.gov/IOTD/view.php?id=5422  </MapURL>
            <SocialNetworkURL>https://www.facebook.com/pages/Great-Flood-of-1993/102266869826690</SocialNetworkURL>
            <Citation>http://www.livescience.com/7508-history-repeats-great-flood-1993.html</Citation>
            <ExternalLinkURL >http://en.wikipedia.org/wiki/Great_Flood_of_1993</ExternalLinkURL>
        </ExternalResources>
        <RelatedOrganizations>
            <RelatedOrganization organizationIdent="NOAA" />
        </RelatedOrganizations>
    </Crisis>
    <Organization organizationIdent="WNG">
            <Name>Wyoming National Guard</Name>
            <Kind organizationKindIdent="MO"></Kind>
            <Location>
                <Locality>Washington D.C.</Locality>
                <Region></Region>
                <Country>United States of America</Country>
            </Location>
            <History>Founded 1870-04-04.</History>
        <ContactInfo>
            <Telephone>3077725241</Telephone>
            <Fax></Fax>
            <Email></Email>
            <PostalAddress><StreetAddress></StreetAddress>
                <Locality></Locality>
                <Region></Region>
                <PostalCode></PostalCode>
                <Country></Country>
            </PostalAddress>
        </ContactInfo>
        <ExternalResources>
            <ImageURL>http://wynga.org/wp-content/uploads/2010/12/Logo.jpg</ImageURL>
            <VideoURL>http://www.youtube.com/watch?v=OvKgS4aViuI</VideoURL>
            <MapURL>http://goo.gl/maps/ho3mA</MapURL>
            <SocialNetworkURL>https://www.facebook.com/USarmy?fref=ts</SocialNetworkURL>
            <Citation>http://www.nytimes.com/1988/08/28/us/1200-more-soldiers-joining-firefighters-in-west.html</Citation>
            <ExternalLinkURL>http://www.nationalguard.com/</ExternalLinkURL>
        </ExternalResources>
        <RelatedCrises>
            <RelatedCrisis crisisIdent="Yellowstone_FR_1988" />
        </RelatedCrises>
    </Organization>
    <Person personIdent="RJoseph">
        <Name>
            <FirstName>Raymond</FirstName>
            <MiddleName></MiddleName>
            <LastName>Joseph</LastName>
            <Suffix></Suffix>
        </Name>
        <Kind personKindIdent="GO"></Kind>
        <Location>
            <Locality>Les Cayes</Locality>
            <Country>Haiti</Country>
        </Location>
        <ExternalResources>
            <ImageURL>http://genesisnetwork.files.wordpress.com/2010/10/m_10260joseph-jpg.jpg</ImageURL>
            <VideoURL>http://youtu.be/Tx3iWRMDWYE</VideoURL>
            <MapURL>https://maps.google.com/maps?hl=en&amp;safe=off&amp;q=les+cayes+haiti&amp;ie=UTF-8&amp;hq=&amp;hnear=0x8ec79c004d1d382d:0xe1470fc907574ec8,Les+Cayes,+Haiti&amp;gl=us&amp;ei=g042UfykDcau2gXNuYCwDA&amp;sqi=2&amp;ved=0CLcBELYD</MapURL>
            <SocialNetworkURL>https://twitter.com/noutoutla</SocialNetworkURL>
            <Citation>>http://baltimorepostexaminer.com/making-haiti-green-again/2013/01/23</Citation>
            <ExternalLinkURL>http://en.wikipedia.org/wiki/Raymond_Joseph</ExternalLinkURL>
        </ExternalResources>
        <RelatedCrises>
            <RelatedCrisis crisisIdent="Haiti_EQ_2010"/>
        </RelatedCrises>
    </Person>
    <CrisisKind crisisKindIdent="ACC">
        <Name>Accident</Name>
        <Description></Description>
    </CrisisKind>
    <OrganizationKind organizationKindIdent="HO">
        <Name>Humanitarian Organization</Name>
        <Description></Description>
    </OrganizationKind>
    <PersonKind personKindIdent="PR">
        <Name>President</Name>
        <Description></Description>
    </PersonKind>
</WorldCrises>""")
        w = StringIO.StringIO()
        WCDB3_solve(r, w)
        self.assert_("""<WorldCrises>
  <Crisis crisisIdent="FL_1993">
    <Name>Great Flood of 1993</Name>
    <Kind crisisKindIdent="FL"/>
    <Location>
      <Locality/>
      <Region>Mississippi, Louisiana, Iowa, Kansas, Minnesota, Missouri, Nebraska</Region>
      <Country>United States of America</Country>
    </Location>
    <StartDateTime>
      <Date>1993-04-01</Date>
      <Time>00:00:00</Time>
    </StartDateTime>
    <EndDateTime>
      <Date>1993-10-01</Date>
      <Time>00:00:00</Time>
    </EndDateTime>
    <HumanImpact>
      <Type/>
      <Number>0</Number>
    </HumanImpact>
    <EconomicImpact>Damages: $15-20 billion</EconomicImpact>
    <ResourceNeeded>Sandbags; Army Corps of Engineers; Army National Guard; American Red Cross</ResourceNeeded>
    <WaysToHelp>Donation to American Red Cross</WaysToHelp>
    <ExternalResources>
      <ImageURL/>
    </ExternalResources>
    <RelatedPersons/>
    <RelatedOrganizations/>
  </Crisis>
  <Organization organizationIdent="WNG">
    <Name>Wyoming National Guard</Name>
    <Kind organizationKindIdent="MO"/>
    <Location>
      <Locality>Washington D.C.</Locality>
      <Country>United States of America</Country>
    </Location>
    <History>Founded 1870-04-04.</History>
    <ContactInfo>
      <Telephone/>
      <Fax/>
      <Email/>
      <PostalAddress>
        <StreetAddress/>
        <Locality>Washington D.C.</Locality>
        <Region/>
        <PostalCode/>
        <Country>United States of America</Country>
      </PostalAddress>
    </ContactInfo>
    <ExternalResources>
      <ImageURL/>
    </ExternalResources>
    <RelatedCrises/>
    <RelatedPersons/>
  </Organization>
  <Person personIdent="RJoseph">
    <Name>
      <FirstName>Raymond</FirstName>
      <LastName>Joseph</LastName>
    </Name>
    <Kind personKindIdent="GO"/>
    <Location>
      <Locality>Les Cayes</Locality>
      <Region/>
      <Country>Haiti</Country>
    </Location>
    <ExternalResources>
      <ImageURL/>
    </ExternalResources>
    <RelatedCrises/>
    <RelatedOrganizations/>
  </Person>
  <CrisisKind crisisKindIdent="ACC">
    <Name>Accident</Name>
    <Description/>
  </CrisisKind>
  <OrganizationKind organizationKindIdent="HO">
    <Name>Humanitarian Organization</Name>
    <Description/>
  </OrganizationKind>
  <PersonKind personKindIdent="PR">
    <Name>President</Name>
    <Description/>
  </PersonKind>
</WorldCrises>

""")

    def test_solve_2 (self) :
        r = StringIO.StringIO("""<?xml version="1.0" ?>
<WorldCrises>
	<Crisis crisisIdent="Yellowstone_FR_1988">
		<Name>Yellowstone Forest Fires of 1988</Name>
		<Kind crisisKindIdent="FR"></Kind>
		<Location>
			<Locality>Yellowstone National Park</Locality>
			<Region>Wyoming</Region>
			<Country>United States of America</Country>
		</Location>
		<StartDateTime><Date>1988-06-23</Date></StartDateTime>
		<EndDateTime><Date>1988-11-18</Date></EndDateTime>
		<HumanImpact>
			<Type>Casualties</Type><Number>2</Number>
		</HumanImpact>
		<EconomicImpact>Structural Damage: $3 million; Money Spent Fighting Fires: $120 million</EconomicImpact>
		<ResourceNeeded>120 helicopters and planes with over 18000 hours of flight time; Over 100 fire engines; 1.4 million gallons of fire retardant; 10 million gallons of water; 9000 firefighters; 4000 US military personell</ResourceNeeded>
		<WaysToHelp>Donation</WaysToHelp>
		<ExternalResources>
			<ImageURL>http://www.thefurtrapper.com/images/Crown%20Fire%20Elk.jpg</ImageURL>
			<VideoURL>http://www.youtube.com/watch?v=4UgLwxK8QDs</VideoURL>
			<MapURL>http://goo.gl/maps/ciql6</MapURL>
			<SocialNetworkURL>https://www.facebook.com/YellowstoneNationalParkVisitor</SocialNetworkURL>
			<Citation>http://usatoday30.usatoday.com/weather/wildfires/2008-08-13-yellowstone-recovers-from-1988-wildfires_N.htm</Citation>
			<ExternalLinkURL>http://en.wikipedia.org/wiki/Yellowstone_fires_of_1988</ExternalLinkURL>
		</ExternalResources>
		<RelatedPersons>
			<RelatedPerson personIdent="GHWBush" />
		</RelatedPersons>
		<RelatedOrganizations>
			<RelatedOrganization organizationIdent="WNG" />
		</RelatedOrganizations>
	</Crisis>
	<Organization organizationIdent="WNG">
			<Name>Wyoming National Guard</Name>
			<Kind organizationKindIdent="MO"></Kind>
			<Location>
				<Locality>Washington D.C.</Locality>
				<Region></Region>
				<Country>United States of America</Country>
			</Location>
			<History>Founded 1870-04-04.</History>
		<ContactInfo>
			<Telephone>3077725241</Telephone>
			<Fax></Fax>
			<Email></Email>
			<PostalAddress><StreetAddress></StreetAddress>
				<Locality></Locality>
				<Region></Region>
				<PostalCode></PostalCode>
			</PostalAddress>
		</ContactInfo>
		<ExternalResources>
			<ImageURL>http://wynga.org/wp-content/uploads/2010/12/Logo.jpg</ImageURL>
			<VideoURL>http://www.youtube.com/watch?v=OvKgS4aViuI</VideoURL>
			<MapURL>http://goo.gl/maps/ho3mA</MapURL>
			<SocialNetworkURL>https://www.facebook.com/USarmy?fref=ts</SocialNetworkURL>
			<Citation>http://www.nytimes.com/1988/08/28/us/1200-more-soldiers-joining-firefighters-in-west.html</Citation>
			<ExternalLinkURL>http://www.nationalguard.com/</ExternalLinkURL>
		</ExternalResources>
		<RelatedCrises>
			<RelatedCrisis crisisIdent="Yellowstone_FR_1988" />
		</RelatedCrises>
			<Locality>Les Cayes</Locality>
	</Organization>
	<Person personIdent="RJoseph">
		<Name>
			<FirstName>Raymond</FirstName>
			<MiddleName></MiddleName>
			<LastName>Joseph</LastName>
			<Suffix></Suffix>
		</Name>
		<Kind personKindIdent="GO"></Kind>
		<Location>
			<Locality>Les Cayes</Locality>
			<Country>Haiti</Country>
		</Location>
		<ExternalResources>
			<ImageURL>http://genesisnetwork.files.wordpress.com/2010/10/m_10260joseph-jpg.jpg</ImageURL>
			<VideoURL>http://youtu.be/Tx3iWRMDWYE</VideoURL>
			<MapURL>https://maps.google.com/maps?hl=en&amp;safe=off&amp;q=les+cayes+haiti&amp;ie=UTF-8&amp;hq=&amp;hnear=0x8ec79c004d1d382d:0xe1470fc907574ec8,Les+Cayes,+Haiti&amp;gl=us&amp;ei=g042UfykDcau2gXNuYCwDA&amp;sqi=2&amp;ved=0CLcBELYD</MapURL>
			<SocialNetworkURL>https://twitter.com/noutoutla</SocialNetworkURL>
			<Citation>>http://baltimorepostexaminer.com/making-haiti-green-again/2013/01/23</Citation>
			<ExternalLinkURL>http://en.wikipedia.org/wiki/Raymond_Joseph</ExternalLinkURL>
		</ExternalResources>
		<RelatedCrises>
			<RelatedCrisis crisisIdent="Haiti_EQ_2010"/>
		</RelatedCrises>
	</Person>
	<CrisisKind crisisKindIdent="ACC">
		<Name>Accident</Name>
		<Description></Description>
	</CrisisKind>
	<OrganizationKind organizationKindIdent="HO">
		<Name>Humanitarian Organization</Name>
		<Description></Description>
	</OrganizationKind>
	<PersonKind personKindIdent="PR">
		<Name>President</Name>
		<Description></Description>
	</PersonKind>
</WorldCrises>""")
        w = StringIO.StringIO()
        WCDB3_solve(r, w)
        self.assert_("""<WorldCrises>
  <Crisis crisisIdent="Yellowstone_FR_1988">
    <Name>Yellowstone Forest Fires of 1988</Name>
    <Kind crisisKindIdent="FR"/>
    <Location>
      <Locality>Yellowstone National Park</Locality>
      <Region>Wyoming</Region>
      <Country>United States of America</Country>
    </Location>
    <StartDateTime>
      <Date>1988-06-23</Date>
      <Time>00:00:00</Time>
    </StartDateTime>
    <EndDateTime>
      <Date>1988-11-18</Date>
      <Time>00:00:00</Time>
    </EndDateTime>
    <HumanImpact>
      <Type/>
      <Number>0</Number>
    </HumanImpact>
    <EconomicImpact>Structural Damage: $3 million; Money Spent Fighting Fires: $120 million</EconomicImpact>
    <ResourceNeeded>120 helicopters and planes with over 18000 hours of flight time; Over 100 fire engines; 1.4 million gallons of fire retardant; 10 million gallons of water; 9000 firefighters; 4000 US military personell</ResourceNeeded>
    <WaysToHelp>Donation</WaysToHelp>
    <ExternalResources>
      <ImageURL/>
    </ExternalResources>
    <RelatedPersons/>
    <RelatedOrganizations/>
  </Crisis>
  <Organization organizationIdent="WNG">
    <Name>Wyoming National Guard</Name>
    <Kind organizationKindIdent="MO"/>
    <Location>
      <Locality>Washington D.C.</Locality>
      <Country>United States of America</Country>
    </Location>
    <History>Founded 1870-04-04.</History>
    <ContactInfo>
      <Telephone/>
      <Fax/>
      <Email/>
      <PostalAddress>
        <StreetAddress/>
        <Locality>Washington D.C.</Locality>
        <Region/>
        <PostalCode/>
        <Country>United States of America</Country>
      </PostalAddress>
    </ContactInfo>
    <ExternalResources>
      <ImageURL/>
    </ExternalResources>
    <RelatedCrises/>
    <RelatedPersons/>
  </Organization>
  <Person personIdent="RJoseph">
    <Name>
      <FirstName>Raymond</FirstName>
      <LastName>Joseph</LastName>
    </Name>
    <Kind personKindIdent="GO"/>
    <Location>
      <Locality>Les Cayes</Locality>
      <Region/>
      <Country>Haiti</Country>
    </Location>
    <ExternalResources>
      <ImageURL/>
    </ExternalResources>
    <RelatedCrises/>
    <RelatedOrganizations/>
  </Person>
  <CrisisKind crisisKindIdent="ACC">
    <Name>Accident</Name>
    <Description/>
  </CrisisKind>
  <OrganizationKind organizationKindIdent="HO">
    <Name>Humanitarian Organization</Name>
    <Description/>
  </CrisisKind>
  <OrganizationKind organizationKindIdent="HO">
    <Name>Humanitarian Organization</Name>
    <Description/>
  </OrganizationKind>
  <PersonKind personKindIdent="PR">
    <Name>President</Name>
    <Description/>
  </PersonKind>
</WorldCrises>""")
        
    def test_solve_3(self):
        w  = StringIO.StringIO()
        r = StringIO.StringIO("""<?xml version="1.0" ?>
<WorldCrises>
    <Crisis crisisIdent="ST_1987">
            <Name>Great Storm of 1987</Name>
            <Kind crisisKindIdent="ST"></Kind>
            <Location>
                <Locality>Cornwall (UK)</Locality>
                <Country>England</Country>
            </Location>
                <StartDateTime><Date>1987-10-15</Date></StartDateTime>
                <EndDateTime><Date>1987-10-16</Date></EndDateTime>
        <HumanImpact><Type>Casualties</Type><Number>22</Number></HumanImpact>
        <EconomicImpact>$24 billion</EconomicImpact>
        <ResourceNeeded>Electricty; Cleaning volunteers</ResourceNeeded>
        <WaysToHelp>Support the UK Forestry COmmission: http://www.forestry.gov.uk/forestry/infd-77ecnd</WaysToHelp>
        <ExternalResources>
            <ImageURL>http://www.marketoracle.co.uk/Article2499.html</ImageURL>
            <VideoURL>http://www.youtube.com/watch?v=Umow5DSrP6E</VideoURL>
            <MapURL>http://goo.gl/maps/Oiu3A</MapURL>
            <SocialNetworkURL>https://www.facebook.com/pages/Great-Storm-of-1987/132425506796646</SocialNetworkURL>
            <Citation>http://www.telegraph.co.uk/earth/earthnews/3307938/Great-Storm-of-1987-twenty-years-on.html</Citation>
            <ExternalLinkURL>http://en.wikipedia.org/wiki/Great_Storm_of_1987</ExternalLinkURL>
        </ExternalResources>        
        <RelatedPersons>
            <RelatedPerson personIdent="BGiles" />
        </RelatedPersons>   
        <RelatedOrganizations>
            <RelatedOrganization organizationIdent="FCGB" />
        </RelatedOrganizations>
    </Crisis>
    <Organization organizationIdent="WNG">
            <Name>Wyoming National Guard</Name>
            <Kind organizationKindIdent="MO"></Kind>
            <Location>
                <Locality>Washington D.C.</Locality>
                <Region></Region>
                <Country>United States of America</Country>
            </Location>
            <History>Founded 1870-04-04.</History>
        <ContactInfo>
            <Telephone>3077725241</Telephone>
            <Fax></Fax>
            <Email></Email>
            <PostalAddress><StreetAddress></StreetAddress>
                <Locality></Locality>
                <Region></Region>
                <PostalCode></PostalCode>
                <Country></Country>
            </PostalAddress>
        </ContactInfo>
        <ExternalResources>
            <ImageURL>http://wynga.org/wp-content/uploads/2010/12/Logo.jpg</ImageURL>
            <VideoURL>http://www.youtube.com/watch?v=OvKgS4aViuI</VideoURL>
            <MapURL>http://goo.gl/maps/ho3mA</MapURL>
            <SocialNetworkURL>https://www.facebook.com/USarmy?fref=ts</SocialNetworkURL>
            <Citation>http://www.nytimes.com/1988/08/28/us/1200-more-soldiers-joining-firefighters-in-west.html</Citation>
            <ExternalLinkURL>http://www.nationalguard.com/</ExternalLinkURL>
        </ExternalResources>
        <RelatedCrises>
            <RelatedCrisis crisisIdent="Yellowstone_FR_1988" />
        </RelatedCrises>
    </Organization>
    <Person personIdent="RJoseph">
        <Name>
            <FirstName>Raymond</FirstName>
            <MiddleName></MiddleName>
            <LastName>Joseph</LastName>
            <Suffix></Suffix>
        </Name>
        <Kind personKindIdent="GO"></Kind>
        <Location>
            <Locality>Les Cayes</Locality>
            <Country>Haiti</Country>
        </Location>
        <ExternalResources>
            <ImageURL>http://genesisnetwork.files.wordpress.com/2010/10/m_10260joseph-jpg.jpg</ImageURL>
            <VideoURL>http://youtu.be/Tx3iWRMDWYE</VideoURL>
            <MapURL>https://maps.google.com/maps?hl=en&amp;safe=off&amp;q=les+cayes+haiti&amp;ie=UTF-8&amp;hq=&amp;hnear=0x8ec79c004d1d382d:0xe1470fc907574ec8,Les+Cayes,+Haiti&amp;gl=us&amp;ei=g042UfykDcau2gXNuYCwDA&amp;sqi=2&amp;ved=0CLcBELYD</MapURL>
            <SocialNetworkURL>https://twitter.com/noutoutla</SocialNetworkURL>
            <Citation>>http://baltimorepostexaminer.com/making-haiti-green-again/2013/01/23</Citation>
            <ExternalLinkURL>http://en.wikipedia.org/wiki/Raymond_Joseph</ExternalLinkURL>
        </ExternalResources>
        <RelatedCrises>
            <RelatedCrisis crisisIdent="Haiti_EQ_2010"/>
        </RelatedCrises>
    </Person>
    <CrisisKind crisisKindIdent="ACC">
        <Name>Accident</Name>
        <Description></Description>
    </CrisisKind>
    <OrganizationKind organizationKindIdent="HO">
        <Name>Humanitarian Organization</Name>
        <Description></Description>
    </OrganizationKind>
    <PersonKind personKindIdent="PR">
        <Name>President</Name>
        <Description></Description>
    </PersonKind>
</WorldCrises>""")
        WCDB3_solve(r, w)
        self.assert_("""<WorldCrises>
  <Crisis crisisIdent="ST_1987">
    <Name>Great Storm of 1987</Name>
    <Kind crisisKindIdent="ST"/>
    <Location>
      <Locality>Cornwall (UK)</Locality>
      <Region/>
      <Country>England</Country>
    </Location>
    <StartDateTime>
      <Date>1987-10-15</Date>
      <Time>00:00:00</Time>
    </StartDateTime>
    <EndDateTime>
      <Date>1987-10-16</Date>
      <Time>00:00:00</Time>
    </EndDateTime>
    <HumanImpact>
      <Type/>
      <Number>0</Number>
    </HumanImpact>
    <EconomicImpact>$24 billion</EconomicImpact>
    <ResourceNeeded>Electricty; Cleaning volunteers</ResourceNeeded>
    <WaysToHelp>Support the UK Forestry COmmission: http://www.forestry.gov.uk/forestry/infd-77ecnd</WaysToHelp>
    <ExternalResources>
      <ImageURL/>
    </ExternalResources>
    <RelatedPersons/>
    <RelatedOrganizations/>
  </Crisis>
  <Organization organizationIdent="WNG">
    <Name>Wyoming National Guard</Name>
    <Kind organizationKindIdent="MO"/>
    <Location>
      <Locality>Washington D.C.</Locality>
      <Country>United States of America</Country>
    </Location>
    <History>Founded 1870-04-04.</History>
    <ContactInfo>
      <Telephone/>
      <Fax/>
      <Email/>
      <PostalAddress>
        <StreetAddress/>
        <Locality>Washington D.C.</Locality>
        <Region/>
        <PostalCode/>
        <Country>United States of America</Country>
      </PostalAddress>
    </ContactInfo>
    <ExternalResources>
      <ImageURL/>
    </ExternalResources>
    <RelatedCrises/>
    <RelatedPersons/>
  </Organization>
  <Person personIdent="RJoseph">
    <Name>
      <FirstName>Raymond</FirstName>
      <LastName>Joseph</LastName>
    </Name>
    <Kind personKindIdent="GO"/>
    <Location>
      <Locality>Les Cayes</Locality>
      <Region/>
      <Country>Haiti</Country>
    </Location>
    <ExternalResources>
      <ImageURL/>
    </ExternalResources>
    <RelatedCrises/>
    <RelatedOrganizations/>
  </Person>
  <CrisisKind crisisKindIdent="ACC">
    <Name>Accident</Name>
    <Description/>
  </CrisisKind>
  <OrganizationKind organizationKindIdent="HO">
    <Name>Humanitarian Organization</Name>
    <Description/>
  </OrganizationKind>
  <PersonKind personKindIdent="PR">
    <Name>President</Name>
    <Description/>
  </PersonKind>
</WorldCrises>""")

# ----
# main
# ----

print("TestWCDB3.py")
unittest.main()
print("Done.")
