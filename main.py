import pandas


def convert_column_to_float64(column_data_frame: pandas.DataFrame,
                              default: float) -> pandas.DataFrame:
    return column_data_frame.apply(
        lambda num:
        num
        if str(num).isnumeric()
        else str(num).replace(",", ".")
        if str(num).replace(",", ".").isnumeric()
        else default
    ).astype("float64")


def convert_column_to_int64(column_data_frame: pandas.DataFrame,
                            default: int) -> pandas.DataFrame:
    return column_data_frame.apply(
        lambda num:
        num
        if str(num).isnumeric()
        else default
    ).astype("int64")


if __name__ == '__main__':

    print(f"\n\nExercícios parte 1\n")

    filename = "./Datasets/Imóveis.csv"

    frame = pandas.read_csv(filename, sep=",")

    print(f"\n{frame.shape}")

    print(f"\n{frame.head(10)}")

    print(f"\n{frame.columns}")

    print(f"\n{frame.dtypes}")

    frame["data"] = pandas.to_datetime(frame["data"])

    frame["análise"] = 2021

    print(f"\n{pandas.DataFrame(frame, columns=['id', 'data', 'preço', 'quartos', 'banheiros', 'ano de construção'])}")

    frame.drop(["metragem da casa.1"], axis=1)  # axis começa em 0, main axis = linha

    frame["banheiros"] = frame["banheiros"].apply(
        lambda num:
        str(num).split(",")[0]
    ).astype('int64')

    print(f"\n{frame.loc[frame['ano de construção'] < 2000]}")

    frame = frame.rename(columns={
        "data": "DT_REFERENCIA",
        "preço": "VL_PRECO",
        "quartos": "QTD_QUARTOS",
        "banheiros": "QTD_BANHEIROS",
        "ano de construção": "DT_ANO_CONSTRUCAO",
        "código postal": "NU_CEP",
        "latitude": "NU_LATITUDE",
        "longitude": "NU_LONGITUDE",
        "andares": "QTD_ANDARES",
        "orla": "FL_ORLA",
        "vista": "FL_VISTA"
    })

    print(f"\n{frame.dtypes}")

    frame["DS_TIPO_CONDICAO"] = [
        "Ruim"
        if num < 2
        else "Regular"
        if num <= 4
        else "Bom"
        for num
        in frame["condição"]
    ]

    print(f"\n{frame['DS_TIPO_CONDICAO']}")

    frame["VL_PRECO"] = frame["VL_PRECO"].apply(
        lambda num:
        str(num).replace(",", ".")
    ).astype('float64')

    print(f"\n{frame[['id', 'VL_PRECO']].sort_values(['VL_PRECO'])}")

    frame_filtro_1 = frame.query("DS_TIPO_CONDICAO == 'Regular'")

    print(f"\n{frame_filtro_1.shape[0]}")

    print(f"\n{frame_filtro_1['VL_PRECO'].mean()}")

    frame_filtro_2 = frame.query("QTD_QUARTOS == 3")

    preco_max = frame_filtro_2['VL_PRECO'].max()

    print(f"\n{preco_max}")

    frame_filtro_3 = frame.query(
        "DS_TIPO_CONDICAO == 'Bom' and QTD_QUARTOS > 2 and QTD_BANHEIROS > 2"
    )

    print(f"\n{frame_filtro_3}")

    preco_max = frame['VL_PRECO'].max()

    frame_casa_maior_preco = frame[frame['VL_PRECO'] == preco_max]

    print(f"\n{frame_casa_maior_preco['id']}")

    preco_min = frame['VL_PRECO'].min()

    frame_casa_menor_preco = frame[frame['VL_PRECO'] == preco_min]

    print(f"\n{frame_casa_menor_preco['id']}")

    print(f"\n{frame['DT_REFERENCIA'].min()}")

    # exercícios parte 2

    print(f"\n\nExercícios parte 2\n")

    print(f"\n{frame.groupby(['DS_TIPO_CONDICAO']).size().reset_index(name='QTD_IMOVEIS')}")

    print(f"\n{frame.groupby(['DT_ANO_CONSTRUCAO'])['VL_PRECO'].mean().reset_index(name='VL_MEDIA')}")

    print(f"\n{frame.groupby(['DT_ANO_CONSTRUCAO'])['QTD_QUARTOS'].min().reset_index(name='NU_MENOR_QUARTOS')}")

    print(f"\n{frame.groupby(['QTD_QUARTOS', 'QTD_BANHEIROS'])['VL_PRECO'].sum().reset_index(name='VL_SOMATORIO')}")

    print(f"\n{frame.groupby(['DT_ANO_CONSTRUCAO'])['VL_PRECO'].median().reset_index(name='VL_MEDIANA')}")

    frame["NU_CLASSIFICACAO_PRECO_1"] = [
        0
        if num < 321950
        else 1
        if num <= 450000
        else 2
        if num <= 645000
        else 3
        for num
        in frame["VL_PRECO"]
    ]

    print(f"\n{frame.head()}")

    frame["NU_CLASSIFICACAO_PRECO_2"] = frame["VL_PRECO"].apply(
        lambda num:
        0
        if num < 321950
        else 1
        if num <= 450000
        else 2
        if num <= 645000
        else 3
    )

    print(f"\n{frame.head()}")

    media_preco = pandas.DataFrame({
        "id": [x for x, y in enumerate(frame.groupby(["NU_CEP"]))],
        "VL_MEDIA_PRECO": frame.groupby(["NU_CEP"])["VL_PRECO"].mean()
    }).reset_index()

    print(f"{media_preco}")

    media_preco.to_csv("./Datasets/Imóveis2.csv", index=False)

    # exercícios parte 3

    print(f"\n\nExercícios parte 3\n")

    path_cadastro_loja_a = "./Datasets/CadastroLoja_A.xlsx"
    path_cadastro_loja_b = "./Datasets/CadastroLoja_B.xlsx"
    path_tipo_cliente = "./Datasets/TipoCliente.xlsx"
    path_vendas = "./Datasets/Vendas.xlsx"

    data_frame_cadastro_loja_a = pandas.DataFrame(
        pandas.read_excel(
            path_cadastro_loja_a
        )
    )

    data_frame_cadastro_loja_b = pandas.DataFrame(
        pandas.read_excel(
            path_cadastro_loja_b
        )
    )

    data_frame_tipo_cliente = pandas.DataFrame(
        pandas.read_excel(
            path_tipo_cliente
        )
    )

    data_frame_vendas = pandas.DataFrame(
        pandas.read_excel(
            path_vendas
        )
    )

    # print(f"\n{data_frame_cadastro_loja_a}")
    # print(f"\n{data_frame_cadastro_loja_b}")
    # print(f"\n{data_frame_tipo_cliente}")
    # print(f"\n{data_frame_vendas}")

    print(f"\nLOJA A:\n{data_frame_cadastro_loja_a.head()}")
    print(f"\n{data_frame_cadastro_loja_a.shape}")
    print(f"\n{data_frame_cadastro_loja_a.dtypes}")

    print(f"\nLOJA B:\n{data_frame_cadastro_loja_b.head()}")
    print(f"\n{data_frame_cadastro_loja_b.shape}")
    print(f"\n{data_frame_cadastro_loja_b.dtypes}")

    print(f"\nTIPO CLIENTE:\n{data_frame_tipo_cliente.head()}")
    print(f"\n{data_frame_tipo_cliente.shape}")
    print(f"\n{data_frame_tipo_cliente.dtypes}")

    print(f"\nVENDAS:\n{data_frame_vendas.head()}")
    print(f"\n{data_frame_vendas.shape}")
    print(f"\n{data_frame_vendas.dtypes}")

    cliente_loja_a_vendas = data_frame_cadastro_loja_a.merge(
        data_frame_vendas,
        how="inner",
        on="ID"
    )

    print(f"\n{cliente_loja_a_vendas}")

    cliente_loja_b_vendas = data_frame_cadastro_loja_b.merge(
        data_frame_vendas,
        how="inner",
        on="ID"
    )

    print(f"\n{cliente_loja_b_vendas}")

    cliente_cadastrado_a_b = data_frame_cadastro_loja_a.merge(
        data_frame_cadastro_loja_b,
        how="inner",
        on="ID"
    ).rename(columns={
        "Nome_x": "NO_A",
        "Nome_y": "NO_B",
        "Idade_x": "NU_IDADE_A",
        "Idade_y": "NU_IDADE_B",
        "CEP_x": "NU_CEP_A",
        "CEP_y": "NU_CEP_B",
        "TipoCliente_x": "CD_TIPO_CLIENTE_A",
        "TipoCliente_y": "CD_TIPO_CLIENTE_B"
    })

    print(f"\n{cliente_cadastrado_a_b}")

    todos_clientes_lojas = data_frame_cadastro_loja_a.merge(
        data_frame_cadastro_loja_b,
        how="outer",
        on="ID",
        suffixes=("_A", "_B")
    ).drop_duplicates(
        subset="ID"
    )

    print(f"\n{todos_clientes_lojas}")

    soma_gastos_clientes_loja_a = data_frame_cadastro_loja_a.merge(
        data_frame_vendas,
        how="inner",
        on="ID"
    )["Valor"].sum()

    print(f"\n{soma_gastos_clientes_loja_a}")

    nome_tipo_cliente_vendas = data_frame_vendas.merge(
        data_frame_cadastro_loja_a.merge(
            data_frame_tipo_cliente,
            how="inner",
            left_on="TipoCliente",
            right_on="ID",
            suffixes=("_A", "_B")
        ),
        how="inner",
        left_on="ID",
        right_on="ID_A"
    ).merge(
        data_frame_cadastro_loja_b.merge(
            data_frame_tipo_cliente,
            how="inner",
            left_on="TipoCliente",
            right_on="ID",
            suffixes=("_A", "_B")
        ),
        how="outer"
    ).drop_duplicates(
        subset="ID_A"
    ).drop(
        ["ID", "Data", "TipoCliente_A", "ID_B"],
        axis=1
    ).rename(
        columns={
            "ID_A": "ID",
            "TipoCliente_B": "TipoCliente"
        }
    ).reset_index().drop(
        ["index"],
        axis=1
    )

    print(f"\n{nome_tipo_cliente_vendas}")

    clientes_loja_a_nao_compraram = data_frame_cadastro_loja_a.merge(
        data_frame_vendas,
        how="left",
        on="ID"
    )

    clientes_loja_a_nao_compraram = clientes_loja_a_nao_compraram[
        clientes_loja_a_nao_compraram["Valor"].isnull()
    ]

    print(f"\n{clientes_loja_a_nao_compraram}")

    clientes_loja_b_nao_compraram = data_frame_cadastro_loja_b.merge(
        data_frame_vendas,
        how="left",
        on="ID"
    )

    clientes_loja_b_nao_compraram = clientes_loja_b_nao_compraram[
        clientes_loja_b_nao_compraram["Valor"].isnull()
    ]

    print(f"\n{clientes_loja_b_nao_compraram}")

    todos_clientes_loja_a_nao_compras = data_frame_vendas.merge(
        data_frame_cadastro_loja_a,
        how="outer",
        on="ID"
    )

    todos_clientes_loja_a_nao_compras = todos_clientes_loja_a_nao_compras[
        todos_clientes_loja_a_nao_compras["Valor"].isnull()
    ]

    todos_clientes_loja_b_nao_compras = data_frame_vendas.merge(
        data_frame_cadastro_loja_b,
        how="outer",
        on="ID"
    )

    todos_clientes_loja_b_nao_compras = todos_clientes_loja_b_nao_compras[
        todos_clientes_loja_b_nao_compras["Valor"].isnull()
    ]

    todos_clientes_lojas_nao_compras = pandas.concat([
        todos_clientes_loja_a_nao_compras,
        todos_clientes_loja_b_nao_compras
    ]).drop_duplicates(
        subset="ID"
    ).drop(
        ["Data", "Valor"],
        axis=1
    )

    print(f"\n{todos_clientes_lojas_nao_compras}")

    todos_clientes_lojas_compras = todos_clientes_lojas.merge(
        data_frame_vendas,
        how="inner",
        on="ID"
    )

    todos_clientes_lojas_compras = todos_clientes_lojas_compras[
        todos_clientes_lojas_compras["Valor"].notnull()
    ]

    print(f"\n{todos_clientes_lojas_compras}")

    tres_mais_compraram = todos_clientes_lojas_compras.sort_values(
        ["Valor"],
        ascending=False
    )[:3]

    print(f"\n{tres_mais_compraram}")
