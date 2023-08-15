import networkx as nx


def nguyen_dupuis(p_ev: float):
    p_gv = 1. - p_ev

    od_graph = nx.DiGraph()
    od_graph.add_edges_from([
        (1, 2, {"trip_rate": 20.0}),
        (1, 3, {"trip_rate": 40.0}),
        (4, 2, {"trip_rate": 30.0}),
        (4, 3, {"trip_rate": 10.0}),
    ])

    gv_od_graph = nx.DiGraph()
    for source, target, data in od_graph.edges(data=True):
        gv_od_graph.add_edge(source, target, trip_rate=data["trip_rate"] * p_gv)

    ev_od_graph = nx.DiGraph()
    for source, target, data in od_graph.edges(data=True):
        ev_od_graph.add_edge(source, target, trip_rate=data["trip_rate"] * p_ev)

    transport_graph = nx.DiGraph()
    transport_graph.add_nodes_from([
        (1, {"type": "regular", "capacity": 0., "time": 0.}),
        (2, {"type": "regular", "capacity": 0., "time": 0.}),
        (3, {"type": "regular", "capacity": 0., "time": 0.}),
        (4, {"type": "regular", "capacity": 0., "time": 0.}),
        (5, {"type": "regular", "capacity": 0., "time": 0.}),
        (6, {"type": "regular", "capacity": 0., "time": 0.}),
        (7, {"type": "virtual", "capacity": 100., "time": 20. / 60.}),
        (8, {"type": "regular", "capacity": 0., "time": 0.}),
        (9, {"type": "virtual", "capacity": 100., "time": 30. / 60.}),
        (10, {"type": "virtual", "capacity": 100., "time": 15. / 60.}),
        (11, {"type": "regular", "capacity": 0., "time": 0.}),
        (12, {"type": "virtual", "capacity": 100., "time": 20. / 60.}),
        (13, {"type": "regular", "capacity": 0., "time": 0.}),
    ])
    transport_graph.add_edges_from([
        (1, 5, {"type": "regular", "capacity": 100., "time": 40. / 60.}),
        (1, 12, {"type": "regular", "capacity": 100., "time": 45. / 60.}),
        (4, 5, {"type": "regular", "capacity": 100., "time": 40. / 60.}),
        (4, 9, {"type": "regular", "capacity": 100., "time": 15. / 60.}),
        (5, 6, {"type": "regular", "capacity": 100., "time": 35. / 60.}),
        (5, 9, {"type": "regular", "capacity": 100., "time": 30. / 60.}),
        (6, 7, {"type": "regular", "capacity": 100., "time": 55. / 60.}),
        (6, 10, {"type": "regular", "capacity": 100., "time": 35. / 60.}),
        (7, 8, {"type": "regular", "capacity": 100., "time": 30. / 60.}),
        (7, 11, {"type": "regular", "capacity": 100., "time": 35. / 60.}),
        (8, 2, {"type": "regular", "capacity": 100., "time": 30. / 60.}),
        (9, 10, {"type": "regular", "capacity": 100., "time": 20. / 60.}),
        (9, 13, {"type": "regular", "capacity": 100., "time": 15. / 60.}),
        (10, 11, {"type": "regular", "capacity": 100., "time": 45. / 60.}),
        (11, 2, {"type": "regular", "capacity": 100., "time": 35. / 60.}),
        (11, 3, {"type": "regular", "capacity": 100., "time": 55. / 60.}),
        (12, 6, {"type": "regular", "capacity": 100., "time": 20. / 60.}),
        (12, 8, {"type": "regular", "capacity": 100., "time": 10. / 60.}),
        (13, 3, {"type": "regular", "capacity": 100., "time": 15. / 60.}),
    ])

    return od_graph, gv_od_graph, ev_od_graph, transport_graph


if __name__ == "__main__":
    od_graph, gv_od_graph, ev_od_graph, transport_graph = nguyen_dupuis(0.5)