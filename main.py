import pandas


if __name__ == '__main__':
    filename = "./Datasets/Imóveis.csv"

    data = pandas.read_csv(filename, sep=",").to_dict()

    frame = pandas.read_csv(filename, sep=",")

    print(f"\n{frame.shape}")

    print(f"\n{frame.head(10)}")

    print(f"\n{frame.columns}")

    print(f"\n{frame.dtypes}")

    frame["data"] = pandas.to_datetime(frame["data"])

    frame["análise"] = 2021

    print(f"\n{pandas.DataFrame(data, columns=['id', 'data', 'preço', 'quartos', 'banheiros', 'ano de construção'])}")

    frame.drop(["metragem da casa.1"], axis=1)  # axis começa em 0, main axis = linha

    frame["banheiros"] = frame["banheiros"].apply(lambda num: str(num).split(",")[0]).astype('int64')

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

    frame["DS_TIPO_CONDICAO"] = ["Ruim" if num < 2 else "Regular" if num <= 4 else "Bom" for num in frame["condição"]]

    print(f"\n{frame['DS_TIPO_CONDICAO']}")

    frame["VL_PRECO"] = frame["VL_PRECO"].apply(lambda num: str(num).replace(",", ".")).astype('float64')

    print(f"\n{frame[['id', 'VL_PRECO']].sort_values(['VL_PRECO'])}")

    frame_filtro_1 = frame.query("DS_TIPO_CONDICAO == 'Regular'")

    print(f"\n{frame_filtro_1.shape[0]}")

    print(f"\n{frame_filtro_1['VL_PRECO'].mean()}")

    frame_filtro_2 = frame.query("QTD_QUARTOS == 3")

    preco_max = frame_filtro_2['VL_PRECO'].max()

    print(f"\n{preco_max}")

    frame_filtro_3 = frame[frame["DS_TIPO_CONDICAO"] == "Bom"]  # Boa não existe

    frame_filtro_3 = frame_filtro_3[frame_filtro_3["QTD_QUARTOS"] > 2]

    frame_filtro_3 = frame_filtro_3[frame_filtro_3["QTD_BANHEIROS"] > 2]

    print(f"\n{frame_filtro_3}")

    preco_max = frame['VL_PRECO'].max()

    frame_casa_maior_preco = frame[frame['VL_PRECO'] == preco_max]

    print(f"\n{frame_casa_maior_preco['id']}")

    preco_min = frame['VL_PRECO'].min()

    frame_casa_menor_preco = frame[frame['VL_PRECO'] == preco_min]

    print(f"\n{frame_casa_menor_preco['id']}")

    print(f"\n{frame['DT_REFERENCIA'].min()}")
