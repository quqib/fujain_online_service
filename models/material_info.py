from sqlalchemy import Column, String, Integer, LargeBinary, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MaterialInfo(Base):
    __tablename__ = 'material_info'

    # 主键与唯一标识
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')
    material_onlycode = Column(String(50), nullable=True, comment='材料唯一编码')
    materialid = Column(String(50), nullable=True, comment='材料版本标识')
    material_code = Column(String(50), nullable=True, comment='材料编码')

    # 关联事项信息
    task_guid = Column(String(50), nullable=True, comment='事项唯一标识')
    task_code = Column(String(36), nullable=True, comment='实施编码')
    ywcode = Column(String(50), nullable=True, comment='业务办理项编码')
    catalog_guid = Column(String(50), nullable=True, comment='目录唯一主键')
    ywcatolog = Column(String(50), nullable=True, comment='业务项目录材料id')

    # 材料基本信息
    material_name = Column(String(200), nullable=True, comment='材料名称')
    material_type = Column(String(2), nullable=True, comment='材料形式')
    material_form = Column(String(2), nullable=True, comment='材料类型')
    is_need = Column(String(2), nullable=True, comment='材料必要性')
    remark = Column(String(200), nullable=True, comment='备注')
    ordernum = Column(Integer, nullable=True, comment='排序号')

    # 材料来源与渠道
    source_type = Column(String(2), nullable=True, comment='来源渠道')
    source_explain = Column(String(500), nullable=True, comment='来源渠道说明')

    # 电子表单与样本
    form_guid = Column(String(500), nullable=True, comment='电子表单（空表）')
    example_guid = Column(String(500), nullable=True, comment='材料样本（样表）')
    is_eform = Column(String(2), nullable=True, comment='是否可从业务表单生成')
    eformName = Column(String(200), nullable=True, comment='关联电子表单名称')
    eformId = Column(String(50), nullable=True, comment='关联电子表单Id')

    # 纸质材料要求
    page_num_y = Column(Integer, nullable=True, comment='原件纸质份数')
    page_num_f = Column(Integer, nullable=True, comment='复印件纸质份数')
    page_format = Column(String(100), nullable=True, comment='纸质材料规格')
    page_f_mark = Column(String(2000), nullable=True, comment='复印件特殊要求')

    # 电子材料要求
    is_bswj = Column(String(2), nullable=True, comment='材料是否版式文件')
    material_format = Column(String(200), nullable=True, comment='允许上传材料格式')
    dzmaterial_format = Column(String(500), nullable=True, comment='电子材料规格')
    is_jgdzyz = Column(String(2), nullable=True, comment='是否加盖电子印章')

    # 填报与受理标准
    fill_explian = Column(String(600), nullable=True, comment='填报须知')
    accept_stand = Column(String(2000), nullable=True, comment='受理标准')
    material_explain = Column(String(1000), nullable=True, comment='材料提交说明')

    # 法律依据
    by_law = Column(LargeBinary, nullable=True, comment='要求提供材料的依据')

    # 电子证照关联
    is_result_cert = Column(String(2), nullable=True, comment='是否电子证照')
    cert_code = Column(String(50), nullable=True, comment='电子证照编码')
    cert_name = Column(String(50), nullable=True, comment='电子证照名称')
    dzzz_catalog_code = Column(String(50), nullable=True, comment='电子证照目录编码')

    # 免提交与数据共享
    is_nocommit = Column(String(2), nullable=True, comment='是否可免提交')
    nocommit_mode = Column(String(50), nullable=True, comment='免交方式')
    is_data_gx = Column(String(2), nullable=True, comment='是否实现数据共享')
    is_sqsjxq = Column(String(2), nullable=True, comment='是否申请数据需求')
    data_need_type = Column(String(1000), nullable=True, comment='数据需求类型')
    data_need_qxtype = Column(String(1000), nullable=True, comment='数据共享形式需求')
    data_gxpl = Column(String(1000), nullable=True, comment='数据更新频率需求')
    data_lyoffice = Column(String(1000), nullable=True, comment='数源部门')

    # 标准材料与层级结构
    basematerialId = Column(String(50), nullable=True, comment='审批结果关联的标准材料id')
    basematerialName = Column(String(200), nullable=True, comment='审批结果关联的标准材料名称')
    basematerial_code = Column(String(50), nullable=True, comment='标准目录编码')
    pid = Column(String(50), nullable=True, comment='一级材料标识')
    relatetype = Column(String(30), nullable=True, comment='关联材料类型')

    # 文件与展示
    icon_image = Column(String(50), nullable=True, comment='缩略图')

    # 审计字段
    create_date = Column(Date, nullable=True, comment='创建日期')
    update_date = Column(Date, nullable=True, comment='更新时间')
    state = Column(String(1), nullable=True, comment='状态')

    def __repr__(self):
        return f"<MaterialInfo(material_name='{self.material_name}', task_code='{self.task_code}')>"