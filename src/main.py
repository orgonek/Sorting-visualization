import click
from data import DataGenerator
from visualizer import Visualizer

@click.group()
def cli():
    pass

@click.command()
@click.option('--data', default='random', help='How the data will be generated (random, reversed, partsorted)', type=str)
@click.argument('algorithm', type=str)
def visualize_algorithm(algorithm, data):
    g = DataGenerator()
    options = ['bubble_sort', 'insertion_sort', 'merge_sort', 'quick_sort', 'selection_sort']
    options_data = {'random': g.random(), 'reversed' : g.reversed(), 'partsorted' : g.part_sorted()}
    
    algorithm = algorithm.lower() if algorithm.lower() in options else 'bubble_sort'
    data= options_data[data.lower()] if data.lower() in options_data.keys() else options_data['random']
    
    v = Visualizer(data)
    v.visualize_algorithm(algorithm)


cli.add_command(visualize_algorithm)

if __name__ == '__main__':
    cli()


