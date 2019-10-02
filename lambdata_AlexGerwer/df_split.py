def train_val_test_split(data, train_portion, val_portion, test_portion):
    # Dependencies
    from sklearn.model_selection import train_test_split

    # Calculate the split
    total_portion = train_portion + val_portion + test_portion
    non_train_portion = val_portion + test_portion

    # round(number[, ndigits])
    train_input = round(train_portion/total_portion, 6)
    non_train_input = round(non_train_portion/total_portion, 6)
    val_input = round(val_portion/non_train_portion, 6)
    test_input = round(test_portion/non_train_portion, 6)

    # Split training and validation data
    train, non_train = train_test_split(data, train_size=train_input,
                                        test_size=non_train_input,
                                        random_state=42)

    # Split the validation and test data
    val, test = train_test_split(non_train, train_size=val_input,
                                 test_size=test_input, random_state=42)

    # Return train, val, test
    return (train, val, test)