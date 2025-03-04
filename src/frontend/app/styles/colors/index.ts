const COLORS = {
    inputBackgroundColor: "#caa165",
    inputBorderColor: "#977a50",
    logoColor: "#582000",
    logoColorStrong: "#370e03",
    black:"#000000",
}

/**
Ajusta o brilho de uma cor hexadecimal.

* Args:
  - hex: Cor hexadecimal a ser ajustada.
  - percent: Porcentagem de ajuste. Valores positivos aumentam o brilho e valores negativos diminuem.

* Returns:
    - Cor hexadecimal ajustada com o brilho.
 **/
export function adjustBrightness(hex: string, percent: number): string {
    // Remove o símbolo # se estiver presente
    hex = hex.replace(/^#/, '');
  
    // Converte a cor hexadecimal para RGB
    let r = parseInt(hex.substring(0, 2), 16);
    let g = parseInt(hex.substring(2, 4), 16);
    let b = parseInt(hex.substring(4, 6), 16);
  
    // Ajusta o brilho
    r = Math.min(255, Math.max(0, r + (r * percent) / 100));
    g = Math.min(255, Math.max(0, g + (g * percent) / 100));
    b = Math.min(255, Math.max(0, b + (b * percent) / 100));
  
    // Converte de volta para hexadecimal
    const newHex = (
      (1 << 24) +
      (r << 16) +
      (g << 8) +
      b
    )
      .toString(16)
      .slice(1)
      .toUpperCase();
  
    return `#${newHex}`;
  }

export default COLORS;