'''
   Copyright (C) 2019  Hermann Mundprecht hmun@thinkthinkdo.com

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software Foundation,
   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

'''

class IAM:
    
    def __init__(self):
        self.map = {
            "0AF" : "XAF" ,
            "0APO" : "XAPO" ,
            "0APO_PPDS" : "XAPO_PPDS" ,
            "0BBP" : "XBBP" ,
            "0BBP_BID" : "XBBP_BID" ,
            "0BWBPCWS" : "XBWBPCWS" ,
            "0BWTCT_BPC" : "XBWTCT_BPC" ,
            "0BWTCT_PLAN" : "XBWTCT_PLAN" ,
            "0BWTCT_PPM" : "XBWTCT_PPM" ,
            "0BWTCT_PPM_VERI" : "XBWTCT_PPM_VERI" ,
            "0BWTCT_PSRV" : "XBWTCT_PSRV" ,
            "0CA" : "XCA" ,
            "0CA_BP" : "XCA_BP" ,
            "0CA_CSM" : "XCA_CSM" ,
            "0CA_IO" : "XCA_IO" ,
            "0CA_PROD" : "XCA_PROD" ,
            "0CA_TIME" : "XCA_TIME" ,
            "0CHANNEL" : "XCHANNEL" ,
            "0CI" : "XCI" ,
            "0CO" : "XCO" ,
            "0COOM" : "XCOOM" ,
            "0COPC" : "XCOPC" ,
            "0COPC_CFS" : "XCOPC_CFS" ,
            "0CP" : "XCP" ,
            "0CPR" : "XCPR" ,
            "0CRM" : "XCRM" ,
            "0CRM_CUST" : "XCRM_CUST" ,
            "0CRM_IO" : "XCRM_IO" ,
            "0CRM_PROD" : "XCRM_PROD" ,
            "0DB" : "XDB" ,
            "0DF" : "XDF" ,
            "0ECC_CRM" : "XECC_CRM" ,
            "0ECPCA" : "XECPCA" ,
            "0EXT_MKT_DATA" : "XEXT_MKT_DATA" ,
            "0FI" : "XFI" ,
            "0FIAA" : "XFIAA" ,
            "0FIAP" : "XFIAP" ,
            "0FIGL" : "XFIGL" ,
            "0FIGL_IO" : "XFIGL_IO" ,
            "0FIN_REP_SIMPL_1_EHP3" : "XFIN_REP_SIMPL_1_EHP3" ,
            "0FIN_REP_SIMPL_1_EHP3_FIGL" : "XFIN_REP_SIMPL_1_EHP3_FIGL" ,
            "0FMCO" : "XFMCO" ,
            "0FS" : "XFS" ,
            "0FSCM" : "XFSCM" ,
            "0FSCM_CR" : "XFSCM_CR" ,
            "0GN" : "XGN" ,
            "0HCM" : "XHCM" ,
            "0IMFA" : "XIMFA" ,
            "0INDUSTRIES" : "XINDUSTRIES" ,
            "0MA" : "XMA" ,
            "0MKTG" : "XMKTG" ,
            "0MKT_MK" : "XMKT_MK" ,
            "0MMIC" : "XMMIC" ,
            "0MMIC_VAL" : "XMMIC_VAL" ,
            "0MMPUR" : "XMMPUR" ,
            "0PAOS" : "XPAOS" ,
            "0PAPA" : "XPAPA" ,
            "0PH" : "XPH" ,
            "0PH_BP" : "XPH_BP" ,
            "0PLM" : "XPLM" ,
            "0PM" : "XPM" ,
            "0PM_TOBJ" : "XPM_TOBJ" ,
            "0PP" : "XPP" ,
            "0PS" : "XPS" ,
            "0PSM" : "XPSM" ,
            "0PSM_FM" : "XPSM_FM" ,
            "0PSM_GM" : "XPSM_GM" ,
            "0PSM_GM_IO" : "XPSM_GM_IO" ,
            "0PS_IO" : "XPS_IO" ,
            "0PT" : "XPT" ,
            "0PY" : "XPY" ,
            "0QM" : "XQM" ,
            "0RT" : "XRT" ,
            "0RT_FASHION" : "XRT_FASHION" ,
            "0RT_FASH_IO" : "XRT_FASH_IO" ,
            "0RT_FOUND" : "XRT_FOUND" ,
            "0SALES" : "XSALES" ,
            "0SAP" : "XSAP" ,
            "0SAPCRM" : "XSAPCRM" ,
            "0SCM" : "XSCM" ,
            "0SCM_TM" : "XSCM_TM" ,
            "0SD" : "XSD" ,
            "0SEM" : "XSEM" ,
            "0SRM" : "XSRM" ,
            "0SRM_PROC" : "XSRM_PROC" ,
            "0TI" : "XTI" ,
            "0TI_RT" : "XTI_RT" ,
            "0TI_RT_MAP" : "XTI_RT_MAP" ,
            "0UC" : "XUC" ,
            "MAGNA_REPORTING_LAYER" : "XAGNA_REPORTING_LAYER" ,
            "NODESNOTCONNECTED" : "NODESNOTCONNECTED" ,
            "ZCO" : "XCO" ,
            "ZCOPC" : "XCOPC" ,
            "ZCOPC_CM" : "XCOPC_CM" ,
            "ZCOPC_D" : "XCOPC_D" ,
            "ZCOPC_V" : "XCOPC_V" ,
            "ZEC0IO" : "XEC0IO" ,
            "ZMM0IO" : "XMM0IO" ,
            "ZPP0IO" : "XPP0IO" ,
            "ZSO0IO" : "XSO0IO" ,
            "ZUE0IO" : "XUE0IO" ,
            "Z_ARCHIV" : "X_ARCHIV" ,
            "Z_BUSINESS_CONTENT_INFOOBJEKTE" : "X_BUSINESS_CONTENT_INFOOBJEKTE" ,
            "Z_EX" : "X_EX" ,
            "Z_EX_EC" : "X_EX_EC" ,
            "Z_EX_EC_PCA" : "X_EX_EC_PCA" ,
            "Z_EX_EC_PCE" : "X_EX_EC_PCE" ,
            "Z_EX_MM" : "X_EX_MM" ,
            "Z_EX_MM_BB" : "X_EX_MM_BB" ,
            "Z_EX_MM_MCKL" : "X_EX_MM_MCKL" ,
            "Z_EX_SD" : "X_EX_SD" ,
            "Z_EX_SD_LIEFERABRUFE" : "X_EX_SD_LIEFERABRUFE" ,
            "Z_EX_UEB" : "X_EX_UEB" ,
            "Z_EX_UEB_MD" : "X_EX_UEB_MD" ,
            "Z_HL1" : "X_HL1" ,
            "Z_HL1MM" : "X_HL1MM" ,
            "Z_HL1MM_BB" : "X_HL1MM_BB" ,
            "Z_HL1MM_DEMAND" : "X_HL1MM_DEMAND" ,
            "Z_HL2" : "X_HL2" ,
            "Z_HL2MM" : "X_HL2MM" ,
            "Z_HL2MM_DEMAND" : "X_HL2MM_DEMAND" ,
            "Z_MAGNA" : "X_MAGNA" ,
            "Z_MAGNA_CHAR" : "X_MAGNA_CHAR" ,
            "Z_MASTERDATA" : "X_MASTERDATA" ,
            "Z_NOT_USE" : "X_NOT_USE" ,
            "Z_R_CO" : "X_R_CO" ,
            "Z_R_CO_COPA" : "X_R_CO_COPA" ,
            "Z_R_CO_COPA_MD" : "X_R_CO_COPA_MD" ,
            "Z_R_CO_EP" : "X_R_CO_EP" ,
            "Z_R_CO_EP_MD" : "X_R_CO_EP_MD" ,
            "Z_R_EC" : "X_R_EC" ,
            "Z_R_EC_PCA" : "X_R_EC_PCA" ,
            "Z_R_EC_PCA_MD" : "X_R_EC_PCA_MD" ,
            "Z_R_EC_PCE" : "X_R_EC_PCE" ,
            "Z_R_MM" : "X_R_MM" ,
            "Z_R_MM_BB" : "X_R_MM_BB" ,
            "Z_R_MM_SEAT_PURCH" : "X_R_MM_SEAT_PURCH" ,
            "Z_R_MM_SEAT_PURCH_MD" : "X_R_MM_SEAT_PURCH_MD" ,
            "Z_R_MTKL_CHKL" : "X_R_MTKL_CHKL" ,
            "Z_R_SD" : "X_R_SD" ,
            "Z_R_SD_AUDIT" : "X_R_SD_AUDIT" ,
            "Z_R_SD_AUDIT_MD" : "X_R_SD_AUDIT_MD" ,
            "Z_R_SD_LIEFERABRUFE" : "X_R_SD_LIEFERABRUFE" ,
            "Z_TRANSFORMATION" : "X_TRANSFORMATION" ,
            "Z_TR_EC" : "X_TR_EC" ,
            "Z_TR_EC_PCE" : "X_TR_EC_PCE" ,
            "Z_TR_MM" : "X_TR_MM" ,
            "Z_TR_MM_BBB" : "X_TR_MM_BBB" ,
            }

    def get_map(self, name):
        split = name.split("::")
        if split[1] in self.map.keys():
            return split[0]+"::"+self.map[split[1]]
        else:
            return name

    def get_short_map(self, name):
        if name in self.map.keys():
            return self.map[name]
        else:
            return name
            
        