import numpy as np

def check_basis_validity(P):
    """
    Safety Check: Ensures the basis actually exists.
    If det = 0, the space is collapsed and can't be used as a basis.
    """
    det = np.linalg.det(P)
    if np.isclose(det, 0.0):
        raise ValueError("CRITICAL ERROR: Invalid Basis! det = 0. This universe is collapsed.")
    return True

def express_in_basis(v_standard, P):
    """
    PORTAL 1: Standard → Alien
    What coordinates does a fixed point have from the alien's perspective?
    Formula: V_alien = P^-1 @ V_standard
    """
    check_basis_validity(P)
    return np.linalg.inv(P) @ v_standard

def back_to_standard(v_alien, P):
    """
    PORTAL 2: Alien → Standard
    Take an alien coordinate and find its true physical location.
    Formula: V_standard = P @ V_alien
    """
    return P @ v_alien

def similarity_transform(M, P):
    """
    THE GOD-MODE EQUATION: P^-1 @ M @ P
    Apply a standard transformation M relative to the alien basis P.
    Same physical action — described in a different coordinate language.
    """
    check_basis_validity(P)
    P_inv = np.linalg.inv(P)
    return P_inv @ M @ P
