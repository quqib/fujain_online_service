from sqlalchemy import Column, String, Integer, Date, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ItemMainInfo(Base):
    __tablename__ = 'item_main_info'

    # 主键（建议数据库中设为主键，即使允许 NULL）
    rowguid = Column(String(50), primary_key=True, nullable=True, comment='主键')

    # 基本信息
    task_name = Column(String(1000), nullable=True, comment='事项名称')
    catalog_code = Column(String(12), nullable=True, comment='基本编码')
    task_code = Column(String(36), nullable=True, comment='实施编码')
    ywcode = Column(String(50), nullable=True, comment='业务办理项编码')
    ywcode_ext = Column(String(100), nullable=True, comment='业务办理项扩展码')
    task_type = Column(String(2), nullable=True, comment='事项类型')

    # 受理与依据
    accept_condition = Column(LargeBinary, nullable=True, comment='受理条件')        # BLOB
    by_law = Column(LargeBinary, nullable=True, comment='设定依据')                # BLOB

    # 行使与状态
    use_level = Column(String(50), nullable=True, comment='行使层级')
    task_state = Column(String(2), nullable=True, comment='事项状态')
    entrust_name = Column(String(100), nullable=True, comment='委托部门')
    project_type = Column(String(2), nullable=True, comment='办件类型')

    # 办结时限
    anticipate_day = Column(String(20), nullable=True, comment='法定办结时限')
    anticipate_type = Column(String(2), nullable=True, comment='法定办结时限单位')
    promise_day = Column(String(20), nullable=True, comment='承诺办结时限')
    promise_type = Column(String(2), nullable=True, comment='承诺办结时限单位')
    promise_day_explain = Column(LargeBinary, nullable=True, comment='承诺办结时限说明')   # BLOB
    anticipate_day_explain = Column(LargeBinary, nullable=True, comment='法定办结时限说明') # BLOB

    # 收费信息
    is_fee = Column(String(2), nullable=True, comment='是否收费')
    charge_by_law = Column(LargeBinary, nullable=True, comment='收费依据')  # BLOB

    # 办理信息
    transact_addr = Column(String(500), nullable=True, comment='办理地点')
    transact_time = Column(String(500), nullable=True, comment='办理时间')
    link_way = Column(String(50), nullable=True, comment='咨询方式')
    supervise_way = Column(String(50), nullable=True, comment='监督投诉方式')

    # 实施主体
    dept_name = Column(String(200), nullable=True, comment='实施主体')
    dept_type = Column(String(2), nullable=True, comment='实施主体性质')
    dept_code = Column(String(20), nullable=True, comment='实施主体编码')

    # 服务与办理形式
    serve_type = Column(String(20), nullable=True, comment='服务对象')
    handle_moder = Column(String(10), nullable=True, comment='办理形式')
    is_need_entry = Column(String(2), nullable=True, comment='计算机端是否对接单点登录')
    login_url = Column(LargeBinary, nullable=True, comment='计算机端在线办理跳转地址')  # BLOB
    is_mobile_entry = Column(String(2), nullable=True, comment='移动端是否对接单点登录')
    transact_app_url = Column(String(500), nullable=True, comment='移动端办理地址')

    # 时间计划
    effectplan = Column(Date, nullable=True, comment='计划生效日期')
    cancelplan = Column(Date, nullable=True, comment='计划取消日期')

    # 权力与流程
    item_source = Column(String(2), nullable=True, comment='权力来源')
    limit_scene_num = Column(Integer, nullable=True, comment='到办事现场次数')
    special_program = Column(String(500), nullable=True, comment='特别程序')
    task_version = Column(String(20), nullable=True, comment='事项版本')
    flow_chart = Column(String(500), nullable=True, comment='办理流程图')
    flow_desc = Column(LargeBinary, nullable=True, comment='办理流程说明')  # BLOB
    impel_agent = Column(String(50), nullable=True, comment='实施机构（科室）')
    is_bak = Column(String(2), nullable=True, comment='是否行政备案')

    # 地址与联系方式扩展
    transact_addr_exp = Column(String(500), nullable=True, comment='办理地点说明')
    link_phone = Column(String(20), nullable=True, comment='咨询电话')
    link_weburl = Column(String(400), nullable=True, comment='咨询网址')
    link_window = Column(String(400), nullable=True, comment='咨询窗口')
    supervise_phone = Column(String(20), nullable=True, comment='监督投诉电话')
    supervise_window = Column(String(400), nullable=True, comment='监督投诉窗口')
    supervise__weburl = Column(String(400), nullable=True, comment='监督投诉网址')  # 注意字段名双下划线

    # 其他属性
    ql_short_name = Column(String(50), nullable=True, comment='日常用语')
    select_type = Column(String(2), nullable=True, comment='查缴办类型')
    version_date = Column(Date, nullable=True, comment='版本时间')
    create_date = Column(Date, nullable=True, comment='创建时间')

    # 版本标识
    item_id = Column(String(50), nullable=True, comment='实施清单版本唯一标识')
    catalog_id = Column(String(50), nullable=True, comment='基本目录版本唯一标识')

    # 区划与发布
    areacode = Column(String(12), nullable=True, comment='区划代码')
    publishstatus = Column(String(2), nullable=True, comment='发布状态')
    publishdate = Column(Date, nullable=True, comment='发布时间')

    # 状态与更新
    state = Column(String(1), nullable=True, comment='状态')
    update_date = Column(Date, nullable=True, comment='更新时间')

    def __repr__(self):
        return f"<ItemMainInfo(task_name={self.task_name[:30] + '...' if self.task_name else 'N/A'}, task_code={self.task_code})>"