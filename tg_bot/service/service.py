import sqlite3
import pika

class Database:
    __DATABASE = 'database.db'

    @classmethod
    def set_filter(cls, user_id: int, setting_name: str, filter: str, filter_id: str = None):
        with sqlite3.connect(cls.__DATABASE) as connect:
            cursor = connect.cursor()
            cursor.execute('SELECT id FROM Settings WHERE name = ?', (setting_name,))
            setting_id = cursor.fetchone()[0]
            cursor.execute(
            'SELECT filter FROM Filters WHERE user_id = ? AND filter = ? AND setting_id = (SELECT id FROM Settings WHERE name = ?)',
            (user_id, filter, setting_name))
            result = cursor.fetchone()
            if not result:
                cursor.execute(
                    'INSERT INTO Filters (user_id, setting_id, filter, filter_id) VALUES (?, ?, ?, ?)',
                    (user_id, setting_id, filter, filter_id))
            else:
                cursor.execute('DELETE FROM Filters WHERE user_id = ? AND filter = ?', (user_id, filter))

    @classmethod
    def get_filters(cls, user_id: int, setting_name: str):
        with sqlite3.connect(cls.__DATABASE) as connect:
            cursor = connect.cursor()
            cursor.execute(
                'SELECT filter FROM Filters WHERE user_id = ? AND setting_id = (SELECT id FROM Settings WHERE name = ?)', (user_id, setting_name))
            filters = [i[0] for i in cursor.fetchall()]
            if not filters:
                filters = []
        return filters
    
    @classmethod
    def clear_filters(cls, user_id: int, setting_id: str):
        with sqlite3.connect(cls.__DATABASE) as connect:
            cursor = connect.cursor()
            cursor.execute('DELETE FROM Filters WHERE user_id = ? AND setting_id = ?', (user_id, int(setting_id)))

    @classmethod
    def get_all_filters(cls, user_id: int, mode: str = 'name'):
        data = {'settings': ''}
        parser_settings = {}
        with sqlite3.connect(cls.__DATABASE) as connect:
            cursor = connect.cursor()
            if mode == 'name':
                with sqlite3.connect(cls.__DATABASE) as connect:
                    cursor = connect.cursor()
                    cursor.execute('SELECT id, name FROM Settings')
                    for i in cursor.fetchall():
                        cursor.execute('SELECT filter, filter_id FROM Filters WHERE user_id = ? AND setting_id = ?', (user_id, i[0]))
                        result = cursor.fetchall()
                        if not result:
                            data['settings'] += f'{i[1]}: []\n'
                        else:
                            data['settings'] += f'{i[1]}: {[j[0] for j in result]}\n'
                return data
            if mode == 'id':
                with sqlite3.connect(cls.__DATABASE) as connect:
                    cursor = connect.cursor()
                    cursor.execute('SELECT id, name FROM Settings')
                    for i in cursor.fetchall():
                        cursor.execute('SELECT filter, filter_id FROM Filters WHERE user_id = ? AND setting_id = ?', (user_id, i[0]))
                        result = cursor.fetchall()
                        if not result:
                            parser_settings[i[1]] = []
                        else:
                            if i[1] in ('Дата регестрации', 'Дата окончания'):
                                parser_settings[i[1]] = [j[0] for j in result][0]
                            else:
                                parser_settings[i[1]] = [j[1] for j in result]
                return parser_settings
           
        
    @classmethod
    def clear_all_filters(cls, user_id: int):
        with sqlite3.connect(cls.__DATABASE) as connect:
            cursor = connect.cursor()
            cursor.execute('DELETE FROM Filters WHERE user_id = ?', (user_id,))

        
class RabbitMQ:
    __HOST = 'amqp://guest:guest@localhost/'

    @classmethod
    def send_status(cls, chat_id: int, message_id: int, message: str):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=pika.PlainCredentials('guest', 'guest')))
        channel = connection.channel()

        channel.queue_declare(queue='requests', durable=True)
        channel.basic_publish(exchange='', routing_key='requests', body=f'{chat_id}:{message_id}:{message}')

        connection.close()


