from sqlalchemy import Column, String, Integer, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CatalogInfo(Base):
    __tablename__ = 'catalog_info'

    # 注意：SQL 中是 `rowguid`，不是主键约束，但这里我们按业务设为可选主键
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')
    task_name = Column(String(10), nullable=True, comment='事项名称/目录名称')
    task_type = Column(String(20), nullable=True, comment='事项类型')
    by_law = Column(LargeBinary, nullable=True, comment='设定依据')  # BLOB -> bytes
    use_level = Column(String(50), nullable=True, comment='行使层级')
    task_state = Column(String(2), nullable=True, comment='事项状态')
    task_version = Column(Integer, nullable=True, comment='事项版本')
    task_code = Column(String(36), nullable=True, comment='基本编码')
    effectplan = Column(Date, nullable=True, comment='计划生效日期')
    cancelplan = Column(Date, nullable=True, comment='计划取消日期')
    sjyw_master = Column(String(20), nullable=True, comment='省级业务主管部门')
    catalog_type = Column(String(50), nullable=True, comment='目录类别')
    is_country_catelog = Column(String(2), nullable=True, comment='是否国家目录')
    is_soncatalog = Column(String(2), nullable=True, comment='是否有子项')
    areacode = Column(String(12), nullable=True, comment='行政区划')
    law_file = Column(LargeBinary, nullable=True, comment='相关法律文件')  # BLOB
    remark = Column(LargeBinary, nullable=True, comment='备注')  # BLOB
    catalog_id = Column(String(50), nullable=True, comment='版本标识')
    parentid = Column(String(50), nullable=True, comment='父项版本标识')
    version_date = Column(Date, nullable=True, comment='版本生效时间')
    businesscodes = Column(String(100), nullable=True, comment='业务条线')
    ordernum = Column(Integer, nullable=True, comment='排序号')
    add_basis = Column(LargeBinary, nullable=True, comment='增补依据')  # BLOB
    user_level_nat_c = Column(String(4000), nullable=True, comment='国家行使内容')
    user_level_pro_c = Column(String(4000), nullable=True, comment='省级专有内容')
    use_level_city_c = Column(String(4000), nullable=True, comment='市级专有内容')
    use_level_county_c = Column(LargeBinary, nullable=True, comment='县级行使内容')  # BLOB
    ql_class_name = Column(String(200), nullable=True, comment='条线分类具体内容')
    if_audit_transer = Column(String(2), nullable=True, comment='是否是审核转报事项')
    audit_transfer_type = Column(String(2), nullable=True, comment='审核转报类型')
    g_fw_content = Column(LargeBinary, nullable=True, comment='服务内容')  # BLOB
    g_fw_mode = Column(String(2), nullable=True, comment='服务方式')
    g_fw_range = Column(String(50), nullable=True, comment='服务领域')
    theme_type = Column(String(40), nullable=True, comment='主题分类')
    trade_type = Column(String(40), nullable=True, comment='行业分类')
    is_yw_catalog = Column(String(2), nullable=True, comment='业务项目录标记')
    fgf_sign = Column(String(1), nullable=True, comment='放管服事项标记')
    create_date = Column(Date, nullable=True, comment='创建时间')
    state = Column(String(1), nullable=True, comment='状态')
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<CatalogInfo(task_name={self.task_name}, task_code={self.task_code})>"

