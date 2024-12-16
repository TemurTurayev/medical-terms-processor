import json

class MedicalElementsProcessor:
    def __init__(self):
        self.medical_terms = self.load_medical_terms()
    
    def load_medical_terms(self):
        """Загрузка медицинских терминов из JSON файла"""
        try:
            with open('medical_terms.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Файл medical_terms.json не найден")
            return {}
    
    def process_text(self, text):
        """
        Обработка текста и поиск медицинских терминов
        
        Args:
            text (str): Текст для анализа
            
        Returns:
            dict: Словарь найденных терминов и их описаний
        """
        found_terms = {}
        for term, description in self.medical_terms.items():
            if term.lower() in text.lower():
                found_terms[term] = description
        return found_terms

def main():
    # Создаем процессор
    processor = MedicalElementsProcessor()
    
    # Пример использования
    text = "У пациента обнаружена гипертензия и тахикардия"
    results = processor.process_text(text)
    
    # Вывод результатов
    print("Найденные медицинские термины:")
    for term, description in results.items():
        print(f"\nТермин: {term}")
        print(f"Описание: {description}")

if __name__ == "__main__":
    main()