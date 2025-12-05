import os
import json
from pathlib import Path
from collections import defaultdict

def analyze_file(file_path):
    """Analisa um arquivo e retorna estatísticas."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            words = content.split()
            
            return {
                'path': str(file_path),
                'chars': len(content),
                'lines': len(lines),
                'words': len(words),
                'size_kb': round(len(content) / 1024, 2),
                'readable': True
            }
    except Exception as e:
        return {
            'path': str(file_path),
            'chars': 0,
            'lines': 0,
            'words': 0,
            'size_kb': 0,
            'readable': False,
            'error': str(e)
        }

def analyze_directory(base_path):
    """Analisa recursivamente todos os arquivos em um diretório."""
    stats = []
    base = Path(base_path)
    
    for file_path in base.rglob('*'):
        if file_path.is_file():
            # Ignora arquivos binários e específicos
            if file_path.suffix in ['.md', '.py', '.ps1', '.json', '.txt', '.yaml', '.yml']:
                stats.append(analyze_file(file_path))
    
    return stats

def generate_report(windsurf_path, specify_path):
    """Gera relatório completo da análise."""
    print("=" * 80)
    print("ANÁLISE QUANTITATIVA DO PROJETO SPEC ORCHESTRATOR")
    print("=" * 80)
    print()
    
    # Analisa ambos os diretórios
    windsurf_stats = analyze_directory(windsurf_path)
    specify_stats = analyze_directory(specify_path)
    
    # Relatório .windsurf
    print("📁 DIRETÓRIO: .windsurf")
    print("-" * 80)
    windsurf_total_chars = sum(s['chars'] for s in windsurf_stats)
    windsurf_total_lines = sum(s['lines'] for s in windsurf_stats)
    windsurf_total_words = sum(s['words'] for s in windsurf_stats)
    
    print(f"Total de arquivos: {len(windsurf_stats)}")
    print(f"Total de caracteres: {windsurf_total_chars:,}")
    print(f"Total de linhas: {windsurf_total_lines:,}")
    print(f"Total de palavras: {windsurf_total_words:,}")
    print(f"Tamanho total: {sum(s['size_kb'] for s in windsurf_stats):.2f} KB")
    print()
    
    # Detalhe por arquivo
    print("Detalhes por arquivo:")
    for stat in sorted(windsurf_stats, key=lambda x: x['chars'], reverse=True):
        rel_path = Path(stat['path']).relative_to(windsurf_path)
        print(f"  • {rel_path}")
        print(f"    Chars: {stat['chars']:,} | Lines: {stat['lines']:,} | Words: {stat['words']:,}")
    
    print()
    print("=" * 80)
    
    # Relatório .specify
    print("📁 DIRETÓRIO: .specify")
    print("-" * 80)
    specify_total_chars = sum(s['chars'] for s in specify_stats)
    specify_total_lines = sum(s['lines'] for s in specify_stats)
    specify_total_words = sum(s['words'] for s in specify_stats)
    
    print(f"Total de arquivos: {len(specify_stats)}")
    print(f"Total de caracteres: {specify_total_chars:,}")
    print(f"Total de linhas: {specify_total_lines:,}")
    print(f"Total de palavras: {specify_total_words:,}")
    print(f"Tamanho total: {sum(s['size_kb'] for s in specify_stats):.2f} KB")
    print()
    
    # Agrupa por subdiretório
    by_subdir = defaultdict(list)
    for stat in specify_stats:
        rel_path = Path(stat['path']).relative_to(specify_path)
        subdir = str(rel_path.parts[0]) if len(rel_path.parts) > 1 else 'root'
        by_subdir[subdir].append(stat)
    
    print("Detalhes por subdiretório:")
    for subdir in sorted(by_subdir.keys()):
        files = by_subdir[subdir]
        total_chars = sum(f['chars'] for f in files)
        print(f"\n  📂 {subdir}/")
        print(f"     Arquivos: {len(files)} | Caracteres: {total_chars:,}")
        for stat in sorted(files, key=lambda x: x['chars'], reverse=True):
            rel_path = Path(stat['path']).relative_to(specify_path)
            print(f"     • {rel_path.name}")
            print(f"       Chars: {stat['chars']:,} | Lines: {stat['lines']:,} | Words: {stat['words']:,}")
    
    print()
    print("=" * 80)
    
    # Resumo Global
    print("📊 RESUMO GLOBAL DO PROJETO")
    print("-" * 80)
    total_files = len(windsurf_stats) + len(specify_stats)
    total_chars = windsurf_total_chars + specify_total_chars
    total_lines = windsurf_total_lines + specify_total_lines
    total_words = windsurf_total_words + specify_total_words
    
    print(f"Total de arquivos analisados: {total_files}")
    print(f"Total de caracteres: {total_chars:,}")
    print(f"Total de linhas: {total_lines:,}")
    print(f"Total de palavras: {total_words:,}")
    print(f"Estimativa de tokens (aprox. chars/4): {total_chars//4:,}")
    print()
    
    # Salva dados em JSON para processamento posterior
    output = {
        'windsurf': {
            'total_files': len(windsurf_stats),
            'total_chars': windsurf_total_chars,
            'total_lines': windsurf_total_lines,
            'total_words': windsurf_total_words,
            'files': windsurf_stats
        },
        'specify': {
            'total_files': len(specify_stats),
            'total_chars': specify_total_chars,
            'total_lines': specify_total_lines,
            'total_words': specify_total_words,
            'files': specify_stats
        },
        'global': {
            'total_files': total_files,
            'total_chars': total_chars,
            'total_lines': total_lines,
            'total_words': total_words,
            'estimated_tokens': total_chars // 4
        }
    }
    
    output_file = Path(__file__).parent / 'docs_analysis.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Análise salva em: {output_file}")
    print("=" * 80)

if __name__ == "__main__":
    base_path = Path(__file__).parent
    windsurf_path = base_path / ".windsurf"
    specify_path = base_path / ".specify"
    
    generate_report(windsurf_path, specify_path)
