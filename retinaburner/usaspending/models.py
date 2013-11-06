from localflavor.us.models import USStateField
from django.db import models
import retinaburner.usaspending

class Contract(models.Model):
    unique_transaction_id = models.CharField(max_length=32, blank=True)
    transaction_status = models.CharField(max_length=32, blank=True)
    obligatedamount = models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=True, null=True)
    baseandexercisedoptionsvalue = models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=True, null=True)
    baseandalloptionsvalue = models.DecimalField(default=0, max_digits=20, decimal_places=2, blank=True, null=True)
    maj_agency_cat = models.CharField(max_length=2, blank=True)
    mod_agency = models.CharField(max_length=4, blank=True)
    maj_fund_agency_cat = models.CharField(max_length=2, blank=True)
    contractingofficeagencyid = models.CharField(max_length=4, blank=True)
    contractingofficeid = models.CharField(max_length=6, blank=True)
    fundingrequestingagencyid = models.CharField(max_length=4, blank=True)
    fundingrequestingofficeid = models.CharField(max_length=6, blank=True)
    fundedbyforeignentity = models.CharField(max_length=21, blank=True)
    signeddate = models.DateField(blank=True, null=True)
    effectivedate = models.DateField(blank=True, null=True)
    currentcompletiondate = models.DateField(blank=True, null=True)
    ultimatecompletiondate = models.DateField(blank=True, null=True)
    lastdatetoorder = models.CharField(max_length=32, blank=True)
    contractactiontype = models.CharField(max_length=4, blank=True)
    reasonformodification = models.CharField(max_length=1, blank=True)
    typeofcontractpricing = models.CharField(max_length=2, blank=True)
    priceevaluationpercentdifference = models.CharField(max_length=100, blank=True)
    subcontractplan = models.CharField(max_length=1, blank=True)
    lettercontract = models.CharField(max_length=1, blank=True)
    multiyearcontract = models.NullBooleanField()
    performancebasedservicecontract = models.CharField(max_length=1, blank=True)
    majorprogramcode = models.CharField(max_length=100, blank=True)
    contingencyhumanitarianpeacekeepingoperation = models.CharField(max_length=1, blank=True)
    contractfinancing = models.CharField(max_length=1, blank=True)
    costorpricingdata = models.CharField(max_length=1, blank=True)
    costaccountingstandardsclause = models.CharField(max_length=1, blank=True)
    descriptionofcontractrequirement = models.TextField(blank=True, null=True)
    purchasecardaspaymentmethod = models.NullBooleanField()
    numberofactions = models.IntegerField(null=True)
    nationalinterestactioncode = models.CharField(max_length=64, blank=True)
    progsourceagency = models.CharField(max_length=2, blank=True)
    progsourceaccount = models.CharField(max_length=4, blank=True)
    progsourcesubacct = models.CharField(max_length=3, blank=True)
    account_title = models.CharField(max_length=255, blank=True)
    rec_flag = models.NullBooleanField()
    typeofidc = models.CharField(max_length=41, blank=True)
    multipleorsingleawardidc = models.CharField(max_length=1, blank=True)
    programacronym = models.CharField(max_length=32, blank=True)
    vendorname = models.CharField(max_length=400, blank=True)
    vendoralternatename = models.CharField(max_length=400, blank=True)
    vendorlegalorganizationname = models.CharField(max_length=400, blank=True)
    vendordoingasbusinessname = models.CharField(max_length=400, blank=True)
    divisionname = models.CharField(max_length=400, blank=True)
    divisionnumberorofficecode = models.CharField(max_length=10, blank=True)
    vendorenabled = models.CharField(max_length=10, blank=True)
    vendorlocationdisableflag = models.NullBooleanField()
    ccrexception = models.CharField(max_length=255, blank=True)
    streetaddress = models.CharField(max_length=400, blank=True)
    streetaddress2 = models.CharField(max_length=400, blank=True)
    streetaddress3 = models.CharField(max_length=400, blank=True)
    city = models.CharField(max_length=35, blank=True)
    state = models.CharField(max_length=35, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    vendorcountrycode = models.CharField(max_length=100, blank=True)
    vendor_state_code = models.CharField(max_length=32, blank=True)
    vendor_cd = models.CharField(max_length=37, blank=True)
    congressionaldistrict = models.CharField(max_length=37, blank=True)
    vendorsitecode = models.CharField(max_length=16, blank=True)
    vendoralternatesitecode = models.CharField(max_length=20, blank=True)
    dunsnumber = models.CharField(max_length=13, blank=True)
    parentdunsnumber = models.CharField(max_length=13, blank=True)
    phoneno = models.CharField(max_length=20, blank=True)
    faxno = models.CharField(max_length=20, blank=True)
    registrationdate = models.DateField(blank=True, null=True)
    renewaldate = models.DateField(blank=True, null=True)
    mod_parent = models.CharField(max_length=100, blank=True)
    locationcode = models.CharField(max_length=5, blank=True)
    statecode = USStateField(blank=True)
    pop_state_code = USStateField(blank=True)
    placeofperformancecountrycode = models.CharField(max_length=3, blank=True)
    placeofperformancezipcode = models.CharField(max_length=10, blank=True)
    pop_cd = models.CharField(max_length=4, blank=True)
    placeofperformancecongressionaldistrict = models.CharField(max_length=6, blank=True)
    psc_cat = models.CharField(max_length=2, blank=True)
    productorservicecode = models.CharField(max_length=4, blank=True)
    systemequipmentcode = models.CharField(max_length=4, blank=True)
    claimantprogramcode = models.CharField(max_length=3, blank=True)
    principalnaicscode = models.CharField(max_length=6, blank=True)
    informationtechnologycommercialitemcategory = models.CharField(max_length=1, blank=True)
    gfe_gfp = models.NullBooleanField()
    useofepadesignatedproducts = models.CharField(max_length=1, blank=True)
    recoveredmaterialclauses = models.CharField(max_length=1, blank=True)
    seatransportation = models.CharField(max_length=1, blank=True)
    contractbundling = models.CharField(max_length=1, blank=True)
    consolidatedcontract = models.NullBooleanField()
    countryoforigin = models.CharField(max_length=3, blank=True)
    placeofmanufacture = models.CharField(max_length=1, blank=True)
    manufacturingorganizationtype = models.CharField(max_length=4, blank=True)
    agencyid = models.CharField(max_length=4, blank=True)
    piid = models.CharField(max_length=50, blank=True)
    modnumber = models.CharField(max_length=25, blank=True)
    transactionnumber = models.CharField(max_length=6, blank=True)
    fiscal_year = models.IntegerField(null=True)
    idvagencyid = models.CharField(max_length=4, blank=True)
    idvpiid = models.CharField(max_length=50, blank=True)
    idvmodificationnumber  = models.CharField(max_length=25, blank=True)
    solicitationid = models.CharField(max_length=25, blank=True)
    extentcompeted = models.CharField(max_length=3, blank=True)
    reasonnotcompeted = models.CharField(max_length=3, blank=True)
    numberofoffersreceived = models.IntegerField(null=True)
    commercialitemacquisitionprocedures = models.CharField(max_length=1, blank=True)
    commercialitemtestprogram = models.NullBooleanField()
    smallbusinesscompetitivenessdemonstrationprogram = models.NullBooleanField()
    a76action = models.NullBooleanField()
    competitiveprocedures = models.CharField(max_length=3, blank=True)
    solicitationprocedures = models.CharField(max_length=5, blank=True)
    typeofsetaside = models.CharField(max_length=10, blank=True)
    localareasetaside = models.CharField(max_length=32, blank=True)
    evaluatedpreference = models.CharField(max_length=6, blank=True)
    fedbizopps = models.CharField(max_length=32, blank=True)
    research = models.CharField(max_length=3, blank=True)
    statutoryexceptiontofairopportunity = models.CharField(max_length=4, blank=True)
    organizationaltype = models.CharField(max_length=64, blank=True)
    numberofemployees = models.IntegerField(null=True)
    annualrevenue = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    firm8aflag = models.NullBooleanField()
    hubzoneflag = models.NullBooleanField()
    sdbflag = models.NullBooleanField()
    shelteredworkshopflag = models.NullBooleanField()
    hbcuflag = models.NullBooleanField()
    educationalinstitutionflag = models.NullBooleanField()
    womenownedflag = models.NullBooleanField()
    veteranownedflag = models.NullBooleanField()
    srdvobflag = models.NullBooleanField()
    localgovernmentflag = models.NullBooleanField()
    minorityinstitutionflag = models.NullBooleanField()
    aiobflag = models.CharField(max_length=1, blank=True)
    stategovernmentflag = models.NullBooleanField()
    federalgovernmentflag = models.NullBooleanField()
    minorityownedbusinessflag = models.NullBooleanField()
    apaobflag = models.NullBooleanField()
    tribalgovernmentflag = models.NullBooleanField()
    baobflag = models.NullBooleanField()
    naobflag = models.NullBooleanField()
    saaobflag = models.NullBooleanField()
    nonprofitorganizationflag = models.NullBooleanField()
    haobflag = models.NullBooleanField()
    emergingsmallbusinessflag = models.NullBooleanField()
    hospitalflag = models.NullBooleanField()
    contractingofficerbusinesssizedetermination = models.CharField(max_length=1, blank=True)
    receivescontracts = models.CharField(max_length=1, blank=True)
    receivesgrants = models.CharField(max_length=1, blank=True)
    receivescontractsandgrants = models.CharField(max_length=1, blank=True)
    walshhealyact = models.NullBooleanField()
    servicecontractact = models.NullBooleanField()
    davisbaconact = models.NullBooleanField()
    clingercohenact = models.NullBooleanField()
    otherstatutoryauthority = models.TextField(blank=True, null=True)
    interagencycontractingauthority = models.CharField(max_length=1, blank=True)
    isserviceprovider = models.NullBooleanField()
    
    agency_name = models.CharField(max_length=255, blank=True)
    contracting_agency_name = models.CharField(max_length=255, blank=True)
    requesting_agency_name = models.CharField(max_length=255, blank=True)
    imported_on = models.DateField(auto_now_add=True)


    