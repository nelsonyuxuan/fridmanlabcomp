#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _DetAMPANMDA_reg();
extern void _DetGABAAB_reg();
extern void _cacumm_reg();
extern void _cagk_reg();
extern void _cal2_reg();
extern void _can2_reg();
extern void _cat_reg();
extern void _h_reg();
extern void _kadist_reg();
extern void _kaprox_reg();
extern void _kca_reg();
extern void _kdb_reg();
extern void _kdrbca1_reg();
extern void _kdrca1_reg();
extern void _kmb_reg();
extern void _na3n_reg();
extern void _naxn_reg();
extern void _vecevent_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," DetAMPANMDA.mod");
fprintf(stderr," DetGABAAB.mod");
fprintf(stderr," cacumm.mod");
fprintf(stderr," cagk.mod");
fprintf(stderr," cal2.mod");
fprintf(stderr," can2.mod");
fprintf(stderr," cat.mod");
fprintf(stderr," h.mod");
fprintf(stderr," kadist.mod");
fprintf(stderr," kaprox.mod");
fprintf(stderr," kca.mod");
fprintf(stderr," kdb.mod");
fprintf(stderr," kdrbca1.mod");
fprintf(stderr," kdrca1.mod");
fprintf(stderr," kmb.mod");
fprintf(stderr," na3n.mod");
fprintf(stderr," naxn.mod");
fprintf(stderr," vecevent.mod");
fprintf(stderr, "\n");
    }
_DetAMPANMDA_reg();
_DetGABAAB_reg();
_cacumm_reg();
_cagk_reg();
_cal2_reg();
_can2_reg();
_cat_reg();
_h_reg();
_kadist_reg();
_kaprox_reg();
_kca_reg();
_kdb_reg();
_kdrbca1_reg();
_kdrca1_reg();
_kmb_reg();
_na3n_reg();
_naxn_reg();
_vecevent_reg();
}
