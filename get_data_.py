import pandas as pd
import pickle


def labeler(current, future): #perceptron
    if float(future) > float(current):
        return 1
    else:
        return 0


main_df = pd.DataFrame()
crypto_names = ["BTC-USD", "LTC-USD", "BCH-USD", "ETH-USD"]
for crypto_name in crypto_names:
    csv_data = f'crypto_data/{crypto_name}.csv'
    df = pd.read_csv(csv_data, names=['time', 'low', 'high', 'open', 'close', 'volume'])
    df.rename(columns={"close": "{}_close".format(crypto_name), "volume": "{}_volume".format(crypto_name)}, inplace=True)
    df.set_index("time", inplace=True)
    df = df[["{}_close".format(crypto_name), "{}_volume".format(crypto_name)]]
    if len(main_df) == 0:
        main_df = df
    else:
        main_df = main_df.join(df)
    main_df["future"] = main_df["{}_close".format(crypto_name)].shift(-2).dropna()
    main_df['labels'] = list(map(labeler,  main_df["{}_close".format(crypto_name)], main_df['future']))
    print(main_df)


