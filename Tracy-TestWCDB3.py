#!/usr/bin/env python

# -------------------------------
# cs327e-wcdb/WCDB3/TestWCDB3.py
# Team Virus
# Copyright (C) 2013
# -------------------------------

"""
To test the program:
    % python TestWCDB3.py >& TestWCDB3.out
    % chmod ugo+x TestWCDB3.py
    % TestWCDB3.py >& TestWCDB3.out
"""


# -------
# imports
# -------

import StringIO
import unittest
import xml.etree.ElementTree as ET


from WCDB3 import *

# ---------
# TestWCDB3
# ---------

class TestWCDB (unittest.TestCase) :

    ############################################
    #             exportToSQL tests            #
    ############################################

    def test_exportToSQL_1 (self) :
        xml =ET.fromstring("""<WorldCrises><Crisis crisisIdent="Chicago_FR_1871">
  <Name>The Great Chicago Fire</Name>
  <Kind crisisKindIdent="FR" />
	<Location>
		<Locality>Chicago</Locality>
		<Region>Illinois</Region>
		<Country>United States</Country>
	</Location>
	<StartDateTime>
		<Date>1871-10-08</Date>
	</StartDateTime>
	<EndDateTime>
	<!-- Optional -->
		<Date>1871-10-10</Date>
	</EndDateTime>
	<HumanImpact>
	<!--Can have multiple -->
		<Type>Casualties</Type>
		<Number>200</Number>
	</HumanImpact>
	<EconomicImpact>222000000</EconomicImpact>
	<ResourceNeeded>Shelter</ResourceNeeded>
	<ResourceNeeded>Food</ResourceNeeded>
	<ResourceNeeded>Medical</ResourceNeeded>
	<WaysToHelp>Donation</WaysToHelp>
	<ExternalResources>
	<!-- all 'external resources' are optional -->
		<VideoURL>http://upload.wikimedia.org/wikipedia/commons/6/6e/Chicago-fire2.jpeg</VideoURL>
	</ExternalResources>
</Crisis></WorldCrises>""")
        returnValue = exportToSQL(xml)
        self.assert_(returnValue == """INSERT IGNORE into Crisis values("Chicago_FR_1871", "The Great Chicago Fire", "FR", "1871-10-08", "null", "1871-10-10", "null", "222000000");""")




    def test_exportToSQL_2 (self) :
        xml =ET.fromstring("""<WorldCrises><Organization organizationIdent="SA">
	<Name>Salvation Army</Name>
	<Kind organizationKindIdent="CO" />
	<Location>
		<Locality>Alexandria</Locality>
		<Region>Virginia</Region>
		<Country>United States</Country>
	</Location>
	<History>Founded in 1865. Founded by a minister and his wife as an aid for the poor, destitute and hungry.</History>
	<ContactInfo>
		<Telephone>8007287825</Telephone>
		<Fax>8007287825</Fax>
		<!-- <Fax>([0-9x+ ]+)?</Fax> -->
		<Email>NHQ_Webmaster@usn.salvationarmy.org</Email>
		<PostalAddress>
			<StreetAddress>615 Slaters Lane</StreetAddress>
			<Locality>Alexandria</Locality>
			<Region>Virginia</Region>
			<PostalCode>22313</PostalCode>
			<Country>United States</Country>
		</PostalAddress>
	</ContactInfo>
	<ExternalResources>
		<ImageURL>https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSXTZ_ZWrimAT2J46Ub2z_5w_efZcU_SaqVis5x4Pd0MbMlY-UMAA</ImageURL>
		<ImageURL>http://blog.salvationarmyusa.org/wp-content/uploads/61.jpg</ImageURL>
		<VideoURL>http://www.youtube.com/watch?v=_ty5A0hj2sI</VideoURL>
		<MapURL>http://3.bp.blogspot.com/_0Q-vLFn_PCk/SjVng0t4daI/AAAAAAAADd0/rH3Z8K2VnAw/s400/earth.jpg</MapURL>
		<SocialNetworkURL>https://www.facebook.com/SalvationArmyUSA</SocialNetworkURL>
		<SocialNetworkURL>https://twitter.com/SalvationArmyUS</SocialNetworkURL>
		<ExternalLinkURL>http://en.wikipedia.org/wiki/The_Salvation_Army</ExternalLinkURL>
	</ExternalResources>
	<RelatedCrises>
		<RelatedCrisis crisisIdent="Japan_EQ_2011" />
		<RelatedCrisis crisisIdent="HU_Katrina_2005" />
		<RelatedCrisis crisisIdent="HU_Andrew_1992" />
		<RelatedCrisis crisisIdent="HU_Ike_2008" />
		<RelatedCrisis crisisIdent="HU_Wilma_2005" />
		<RelatedCrisis crisisIdent="HU_Ivan_2004" />
		<RelatedCrisis crisisIdent="HU_Charley_2004" />
		<RelatedCrisis crisisIdent="HU_Sandy_2012" />
		<RelatedCrisis crisisIdent="Tri-State_TO_1925" />
	</RelatedCrises>
</Organization></WorldCrises>""")
        returnValue = exportToSQL(xml)
        self.assert_(returnValue == """INSERT IGNORE into Organization values("SA", "Salvation Army", "CO", "Founded in 1865. Founded by a minister and his wife as an aid for the poor, destitute and hungry.", "8007287825", "8007287825", "NHQ_Webmaster@usn.salvationarmy.org", "615 Slaters Lane", "Alexandria", "Virginia", "22313", "United States");""")



    def test_exportToSQL_3 (self) :
        xml =ET.fromstring("""<WorldCrises><PersonKind personKindIdent="AMB">
<Name>United States Ambassador</Name>
<Description>An accredited diplomat sent by a country as its official representative to a foreign country.</Description>
</PersonKind></WorldCrises>""")
        returnValue = exportToSQL(xml)
        self.assert_(returnValue == """INSERT IGNORE into PersonKind values("AMB", "United States Ambassador", "An accredited diplomat sent by a country as its official representative to a foreign country.");""")


    ############################################
    #                login tests               #
    ############################################

    def test_login_1 (self) :
        c = login(
            "z",
            "tracy",
            "mfTTR8Puk5",
            "cs327e_tracy")
        assert str(type(c)) == "<type '_mysql.connection'>"

    def test_login_2 (self) :
        c = login(
            "z",
            "amtul",
            "bhoe8w2M2b",
            "cs327e_amtul")
        assert str(type(c)) == "<type '_mysql.connection'>"

    def test_login_3 (self) :
        c = login()
        assert str(type(c)) == "<type '_mysql.connection'>"

    ############################################
    #                query tests               #
    ############################################

    def test_query_1 (self) :
        c = query(login(),"show Tables")
        assert c == None

    def test_query_2 (self) :
        c = query(login(),"select * from CrisisKind")
        assert c == None

    def test_query_3 (self) :
        c = query(login(),"show Databases")
        assert c == None

    ############################################
    #            main/create tests             #
    ############################################

    def test_main_1 (self) :
        c = main("WCDB3.xml","out.txt")
        assert c == None


    def test_createTables_1 (self) :
        returnValue = createTables()
        self.assert_(returnValue == None)

print "TestWCDB3.py"
unittest.main()
print "Done."
