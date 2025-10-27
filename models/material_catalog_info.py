from sqlalchemy import Column, String, Integer, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MaterialCatalogInfo(Base):
    __tablename__ = 'material_catalog_info'

    # 主键（建议数据库中设为主键）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 关联字段
    catalog_guid = Column(String(50), nullable=True, comment='目录唯一主键')
    task_code = Column(String(36), nullable=True, comment='实施编码')
    ywcode = Column(String(50), nullable=True, comment='业务办理项编码')
    ywcode_ext = Column(String(100), nullable=True, comment='业务办理项扩展码')

    # 材料基本信息
    material_name = Column(String(200), nullable=True, comment='材料名称')
    material_type = Column(String(2), nullable=True, comment='材料形式')  # 如：原件、复印件
    material_form = Column(String(2), nullable=True, comment='材料类型')  # 如：证照、申请表等
    is_need = Column(String(2), nullable=True, comment='材料必要性')      # 是否必须提供

    # 文件资源链接
    form_guid = Column(String(500), nullable=True, comment='空白表格')       # 空白表格文件路径或GUID
    example_guid = Column(String(500), nullable=True, comment='示例样表')     # 示例样表文件路径或GUID

    # 来源信息
    source_type = Column(String(2), nullable=True, comment='来源渠道')        # 如：申请人自备、政府部门核发
    source_explain = Column(String(500), nullable=True, comment='来源渠道说明')

    # 纸质材料要求
    page_num_y = Column(Integer, nullable=True, comment='原件纸质份数')
    page_num_f = Column(Integer, nullable=True, comment='复印件纸质份数')
    page_format = Column(String(200), nullable=True, comment='纸质材料规格')   # 如 A4、A3

    # 填报与受理标准
    material_tbxz = Column(String(500), nullable=True, comment='填报须知')
    material_slbz = Column(String(500), nullable=True, comment='受理标准')

    # 法律依据
    by_law = Column(LargeBinary, nullable=True, comment='要求提供材料的依据')  # BLOB 类型，存储文本或富文本

    # 版本标识
    materialid = Column(String(50), nullable=True, comment='材料版本标识')

    # 电子证照相关
    is_result_cert = Column(String(2), nullable=True, comment='是否电子证照')
    cert_code = Column(String(50), nullable=True, comment='电子证照编码')
    cert_name = Column(String(50), nullable=True, comment='电子证照名称')
    icon_image = Column(String(50), nullable=True, comment='缩略图')  # 图标/缩略图路径

    # 层级与关联信息
    pid = Column(String(50), nullable=True, comment='一级材料标识')  # 父级材料 ID，用于树形结构
    eformName = Column(String(200), nullable=True, comment='关联电子表单名称')
    eformId = Column(String(50), nullable=True, comment='关联电子表单Id')

    # 审批结果关联
    basematerialId = Column(String(50), nullable=True, comment='审批结果关联的标准材料id')
    basematerialName = Column(String(200), nullable=True, comment='审批结果关联的标准材料名称')
    relatetype = Column(String(50), nullable=True, comment='关联材料类型')

    # 其他字段
    remark = Column(String(200), nullable=True, comment='备注')
    ordernum = Column(Integer, nullable=True, comment='排序号')  # 用于前端展示顺序

    # 时间与状态
    create_date = Column(Date, nullable=True, comment='创建日期')
    state = Column(String(1), nullable=True, comment='状态')  # 如：1-有效，0-无效
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<MaterialCatalogInfo(material_name={self.material_name}, task_code={self.task_code})>"