"""
El Salvador News Scraper - Versión Simplificada
AI Para Todos - Vibe Coding Workshop
Cursor AI Advanced Coding Project

Este proyecto demuestra web scraping básico usando datos de ejemplo.
This project demonstrates basic web scraping using sample data.
"""

import pandas as pd
import json
from datetime import datetime
import random

class ElSalvadorNewsScraper:
    """
    Clase para simular extracción de noticias de El Salvador
    Class to simulate news extraction from El Salvador
    """
    
    def __init__(self):
        """Inicializar el scraper de noticias"""
        self.news_data = []
        
    def create_sample_data(self):
        """
        Crear datos de ejemplo de noticias
        Create sample news data
        """
        print("📰 Creando datos de ejemplo de noticias...")
        print("📰 Creating sample news data...")
        
        # Datos de ejemplo de noticias
        # Sample news data
        sample_news = [
            {
                "title": "Nuevo proyecto de tecnología en San Salvador",
                "content": "El gobierno anunció un nuevo proyecto de tecnología que beneficiará a miles de estudiantes en la capital.",
                "source": "elsalvador.com",
                "category": "Tecnología",
                "date": "2024-01-15"
            },
            {
                "title": "Inauguración del nuevo centro comercial",
                "content": "Se inauguró el centro comercial más grande de El Salvador, creando cientos de empleos.",
                "source": "elsalvador.com",
                "category": "Economía",
                "date": "2024-01-14"
            },
            {
                "title": "Éxito en el torneo de fútbol nacional",
                "content": "El equipo nacional logró una victoria importante en el torneo regional.",
                "source": "diarioelmundo.com.sv",
                "category": "Deportes",
                "date": "2024-01-13"
            },
            {
                "title": "Avances en educación digital",
                "content": "Las escuelas públicas implementan nuevas tecnologías para mejorar la educación.",
                "source": "diarioelmundo.com.sv",
                "category": "Educación",
                "date": "2024-01-12"
            },
            {
                "title": "Nuevas oportunidades de empleo",
                "content": "Se anunciaron más de 500 nuevas posiciones en el sector tecnológico.",
                "source": "elsalvador.com",
                "category": "Empleo",
                "date": "2024-01-11"
            }
        ]
        
        # Agregar datos de ejemplo a la lista
        # Add sample data to the list
        for news in sample_news:
            news["scraped_at"] = datetime.now().isoformat()
            self.news_data.append(news)
        
        print(f"✅ Se crearon {len(self.news_data)} noticias de ejemplo")
        print(f"✅ Created {len(self.news_data)} sample news articles")
        
    def analyze_news(self):
        """
        Analizar las noticias
        Analyze the news
        """
        if not self.news_data:
            print("❌ No hay datos para analizar")
            print("❌ No data to analyze")
            return
        
        print("\n📊 ANÁLISIS DE NOTICIAS")
        print("📊 NEWS ANALYSIS")
        print("=" * 50)
        
        # Crear DataFrame
        # Create DataFrame
        df = pd.DataFrame(self.news_data)
        
        print(f"📈 Total de artículos: {len(df)}")
        print(f"📈 Total articles: {len(df)}")
        
        print(f"\n📰 Fuentes de noticias:")
        print(f"📰 News sources:")
        print(df['source'].value_counts())
        
        print(f"\n📂 Categorías de noticias:")
        print(f"📂 News categories:")
        print(df['category'].value_counts())
        
        # Análisis de longitud de contenido
        # Content length analysis
        df['content_length'] = df['content'].str.len()
        
        print(f"\n📏 Estadísticas de longitud de contenido:")
        print(f"📏 Content length statistics:")
        print(f"   Promedio / Average: {df['content_length'].mean():.0f} caracteres")
        print(f"   Máximo / Maximum: {df['content_length'].max():.0f} caracteres")
        print(f"   Mínimo / Minimum: {df['content_length'].min():.0f} caracteres")
        
        return df
    
    def save_data(self, filename=None):
        """
        Guardar datos
        Save data
        """
        if not self.news_data:
            print("❌ No hay datos para guardar")
            print("❌ No data to save")
            return
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"elsalvador_news_{timestamp}"
        
        # Guardar como JSON
        # Save as JSON
        json_filename = f"{filename}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(self.news_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Datos guardados como JSON: {json_filename}")
        print(f"✅ Data saved as JSON: {json_filename}")
        
        # Guardar como CSV
        # Save as CSV
        df = pd.DataFrame(self.news_data)
        csv_filename = f"{filename}.csv"
        df.to_csv(csv_filename, index=False, encoding='utf-8')
        
        print(f"✅ Datos guardados como CSV: {csv_filename}")
        print(f"✅ Data saved as CSV: {csv_filename}")
        
        return json_filename, csv_filename
    
    def display_news(self):
        """
        Mostrar las noticias de forma organizada
        Display news in organized format
        """
        if not self.news_data:
            print("❌ No hay datos para mostrar")
            print("❌ No data to display")
            return
        
        print("\n📰 NOTICIAS DE EL SALVADOR")
        print("📰 EL SALVADOR NEWS")
        print("=" * 60)
        
        for i, news in enumerate(self.news_data, 1):
            print(f"\n📄 Artículo {i}:")
            print(f"📄 Article {i}:")
            print(f"   📰 Título / Title: {news['title']}")
            print(f"   📝 Contenido / Content: {news['content']}")
            print(f"   🏢 Fuente / Source: {news['source']}")
            print(f"   📂 Categoría / Category: {news['category']}")
            print(f"   📅 Fecha / Date: {news['date']}")
            print("-" * 40)

def main():
    """
    Función principal para ejecutar el scraper
    Main function to run the scraper
    """
    print("🇸🇻 EL SALVADOR NEWS SCRAPER - VERSIÓN SIMPLIFICADA")
    print("🇸🇻 AI Para Todos - Vibe Coding Workshop")
    print("=" * 60)
    
    # Crear instancia del scraper
    # Create scraper instance
    scraper = ElSalvadorNewsScraper()
    
    # Crear datos de ejemplo
    # Create sample data
    scraper.create_sample_data()
    
    # Mostrar noticias
    # Display news
    scraper.display_news()
    
    # Analizar datos
    # Analyze data
    df = scraper.analyze_news()
    
    # Guardar datos
    # Save data
    if scraper.news_data:
        json_file, csv_file = scraper.save_data()
        
        print(f"\n🎉 ¡Scraping completado exitosamente!")
        print(f"🎉 Scraping completed successfully!")
        print(f"\n📁 Archivos generados / Generated files:")
        print(f"   - {json_file}")
        print(f"   - {csv_file}")
        
        print(f"\n💡 Próximos pasos / Next steps:")
        print(f"   - Analizar los datos con pandas")
        print(f"   - Crear visualizaciones con matplotlib")
        print(f"   - Construir un dashboard de noticias")
        print(f"   - Agregar análisis de sentimientos")
    else:
        print(f"\n❌ No se pudieron crear noticias")
        print(f"❌ Could not create news")

if __name__ == "__main__":
    main() 