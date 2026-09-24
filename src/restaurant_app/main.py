import restaurant

def get_user_name():
    return input('こんにちは、私はRoboko！あなたの名前は？')

def get_favorite_restaurant(name):
    return input(f'{name}さん、どこのレストランが好き？')

def say_goodbye(name):
    print(f'{name}さん。ありがとう！\n'
              '良い1日を！')

def main():

    # 名前を聞く
    name = get_user_name()

    restaurant_csv = restaurant.get_restaurant_csv_path()

    #　ファイルがもし存在すれば、CSVを開き、辞書型として行ごとに保存
    recommend_rows = restaurant.load_restaurants(restaurant_csv)       

        #　CSVファイルにあるレストラン名が好きか、降順で聞く
    restaurant.recommend_restaurant(recommend_rows)

    # 好きなレストランを聞く
    favorite_restaurant = get_favorite_restaurant(name)
    #　好きなレストランがこれまであれば、1足して、なければ新たな辞書型リストを追加
    new_resutaurant_rows = restaurant.update_restaurant_count(recommend_rows, favorite_restaurant)

    #　更新したレストランデータをCSVに書き込む
    restaurant.save_restaurants(restaurant_csv, new_resutaurant_rows)

    say_goodbye(name)

main()