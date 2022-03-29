from schedule.streams.IT.bvt import get_full_schedule_bvt, get_schedule_bvt
from schedule.streams.IT.bst import get_full_schedule_bst, get_schedule_bst
from schedule.streams.IT.bei import get_full_schedule_bei, get_schedule_bei
from schedule.streams.IT.bfi import get_full_schedule_bfi, get_schedule_bfi
from schedule.streams.KIIB.bib import get_full_schedule_bib, get_schedule_bib
from schedule.streams.KIIB.bmp import get_full_schedule_bmp, get_schedule_bmp
from schedule.streams.KIIB.zrc import get_full_schedule_zrc, get_schedule_zrc
from schedule.streams.KIIB.bap import get_full_schedule_bap, get_schedule_bap
from schedule.streams.KIIB.but import get_full_schedule_but, get_schedule_but
from schedule.streams.RIT.brt import get_full_schedule_brt, get_schedule_brt
from schedule.streams.RIT.bik import get_full_schedule_bik, get_schedule_bik
from schedule.streams.TCEIMK.bee import get_full_schedule_bee, get_schedule_bee
from schedule.streams.TCEIMK.bbi import get_full_schedule_bbi, get_schedule_bbi
from schedule.streams.TCEIMK.ber import get_full_schedule_ber, get_schedule_ber

group_matching_schedule = {
        'бвт' : get_schedule_bvt,
        'бст' : get_schedule_bst,
        'бэи' : get_schedule_bei,
        'бфи' : get_schedule_bfi,
        'бап' : get_schedule_bap,
        'биб' : get_schedule_bib,
        'бмп' : get_schedule_bmp,
        'бут' : get_schedule_but,
        'бик' : get_schedule_bik,
        'брт' : get_schedule_brt,
        'бби' : get_schedule_bbi,
        'бээ' : get_schedule_bee,
        'бэр' : get_schedule_ber

}
group_matching_full_schedule = {
        'бвт' : get_full_schedule_bvt,
        'бст' : get_full_schedule_bst,
        'бэи' : get_full_schedule_bei,
        'бфи' : get_full_schedule_bfi,
        'бап' : get_full_schedule_bap,
        'биб' : get_full_schedule_bib,
        'бмп' : get_full_schedule_bmp,
        'бут' : get_full_schedule_but,
        'бик' : get_full_schedule_bik,
        'брт' : get_full_schedule_brt,
        'бби' : get_full_schedule_bbi,
        'бээ' : get_full_schedule_bee,
        'бэр' : get_full_schedule_ber

}