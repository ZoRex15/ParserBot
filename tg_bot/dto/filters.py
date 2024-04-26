from dataclasses import dataclass, field
from typing import List

@dataclass
class FiltersDTO:
    count_requests: int
    status: List[str] = field(default_factory=list)
    zayvitel: List[str] = field(default_factory=list)
    tech_reg: List[str] = field(default_factory=list)
    type_decl: List[str] = field(default_factory=list)
    type_obj_decl: List[str] = field(default_factory=list)
    proizhodenie_product: List[str] = field(default_factory=list)
    edini_perechen_product_eaes: List[str] = field(default_factory=list)
    edini_perechen_product_rf: List[str] = field(default_factory=list)
    reg_date_min: str = ''
    reg_date_max: str = ''
    end_date_min: str = ''
    end_date_max: str = ''
    group_product_rf: List[str] = field(default_factory=list)
    group_product_eaes: List[str] = field(default_factory=list)
