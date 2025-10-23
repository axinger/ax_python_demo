import duckdb


def left_join_mysql_tables_simple():
    try:
        conn = duckdb.connect()

        # 加载MySQL扩展
        # try:
        #     conn.execute("LOAD mysql")
        # except:
        #     conn.execute("INSTALL mysql")
        #     conn.execute("LOAD mysql")

        try:
            conn.execute("LOAD mysql")
        except duckdb.Error:
            try:
                conn.execute("INSTALL mysql")
                conn.execute("LOAD mysql")
            except duckdb.Error as e:
                print(f"MySQL扩展安装或加载失败: {e}")
                raise
        # 连接两个MySQL数据库
        conn.execute(
            "ATTACH 'host=localhost port=3306 user=root password=Abcd#1234 database=ax_test01' AS db1 (TYPE mysql)")
        conn.execute(
            "ATTACH 'host=localhost port=3306 user=root password=Abcd#1234 database=ax_test02' AS db2 (TYPE mysql)")

        # 执行LEFT JOIN
        query = """
                SELECT a.id, a.name, b.id AS id2, b.name AS name2
                FROM db1.order_person a
                         LEFT JOIN db2.order_person b ON a.id = b.id \
                """

        # 直接返回结果集
        result_set = conn.execute(query)
        # 获取所有结果
        results = result_set.fetchall()
        columns = [desc[0] for desc in result_set.description]

        conn.close()

        return columns, results

    except Exception as e:
        print(f"错误: {e}")
        return None, None


# 使用
if __name__ == "__main__":
    head, data = left_join_mysql_tables_simple()
    if data:
        print("LEFT JOIN结果:")
        print("列:", head)
        for i, row in enumerate(data[:5]):  # 显示前5行
            print(f"行 {i + 1}: {row}")
        print(f"总行数: {len(data)}")