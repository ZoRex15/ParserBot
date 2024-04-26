import sqlite3
import pika

class Database:
    def __init__(self, session: sqlite3.Connection):
        self.session = session

    def set_filter(self, user_id: int, setting_name: str, filter: str, filter_id: str = None):
        cursor = self.session.cursor()
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

    def get_filters(self, user_id: int, setting_name: str):
        cursor = self.session.cursor()
        cursor.execute(
            'SELECT filter FROM Filters WHERE user_id = ? AND setting_id = (SELECT id FROM Settings WHERE name = ?)', (user_id, setting_name))
        filters = [i[0] for i in cursor.fetchall()]
        if not filters:
            filters = []
        return filters
    
    def clear_filters(self, user_id: int, setting_id: str):
        cursor = self.session.cursor()
        cursor.execute('DELETE FROM Filters WHERE user_id = ? AND setting_id = ?', (user_id, int(setting_id)))

    def get_all_filters(self, user_id: int, mode: str = 'name'):
        data = {'settings': ''}
        parser_settings = {}
        cursor = self.session.cursor()
        if mode == 'name':
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
            cursor.execute('SELECT id, name FROM Settings')
            for i in cursor.fetchall():
                cursor.execute('SELECT filter, filter_id FROM Filters WHERE user_id = ? AND setting_id = ?', (user_id, i[0]))
                result = cursor.fetchall()
                if not result:
                    parser_settings[i[1]] = []
                elif i[1] in ('Дата регестрации', 'Дата окончания'):
                    parser_settings[i[1]] = [j[0] for j in result][0]
                elif i[1] == 'Номер сертификата':
                    parser_settings[i[1]] = [j[0] for j in result]
                else:
                    parser_settings[i[1]] = [j[1] for j in result]
            return parser_settings
           
    def clear_all_filters(self, user_id: int):
            cursor = self.session.cursor()
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


