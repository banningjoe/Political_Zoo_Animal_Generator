from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

from constants import PoliticalPositions, POLITICAL_PLATFORMS


def load_image(filepath: Path) -> Image.Image:
    return Image.open(filepath).convert('RGBA')


def create_white_background_with_shrunk_image(original_image: Image.Image, shrink_factor: float = 0.6) -> Image.Image:
    original_width, original_height = original_image.size
    
    white_background = Image.new('RGBA', (original_width, original_height), (255, 255, 255, 255))
    
    new_width = int(original_width * shrink_factor)
    new_height = int(original_height * shrink_factor)
    
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
    
    x_offset = (original_width - new_width) // 2
    y_offset = (original_height - new_height) // 2
    
    white_background.paste(resized_image, (x_offset, y_offset), resized_image)
    
    return white_background


def get_cute_font(size: int) -> ImageFont.FreeTypeFont:
    font_options = [
        'Chalkboard',
        'ChalkboardSE-Regular',
        '/System/Library/Fonts/Chalkboard.ttc',
        'Comic Sans MS',
        'Arial Rounded MT Bold',
        'Arial'
    ]
    
    for font_name in font_options:
        try:
            return ImageFont.truetype(font_name, size)
        except (OSError, IOError):
            continue
    
    return ImageFont.load_default()


def format_positions_text(name: str, positions: PoliticalPositions) -> list[str]:
    lines = []
    
    for_list = [p.value for p in positions["FOR"]]
    against_list = [p.value for p in positions["AGAINST"]]
    
    for_unique = []
    seen_for = set()
    for position in for_list:
        if position not in seen_for:
            for_unique.append(position)
            seen_for.add(position)
    
    against_unique = []
    seen_against = set()
    for position in against_list:
        if position not in seen_against:
            against_unique.append(position)
            seen_against.add(position)
    
    lines.append("FOR:")
    if for_unique:
        for position in for_unique:
            lines.append(f"  {position}")
    else:
        lines.append("  Nothing")
    
    lines.append("")
    lines.append("AGAINST:")
    if against_unique:
        for position in against_unique:
            lines.append(f"  {position}")
    else:
        lines.append("  Nothing")
    
    return lines


def calculate_text_dimensions(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height


def calculate_multiline_text_dimensions(draw: ImageDraw.ImageDraw, lines: list[str], font: ImageFont.FreeTypeFont, line_spacing: int = 10) -> tuple[int, int]:
    max_width = 0
    total_height = 0
    
    for i, line in enumerate(lines):
        width, height = calculate_text_dimensions(draw, line, font)
        max_width = max(max_width, width)
        total_height += height
        if i < len(lines) - 1:
            total_height += line_spacing
    
    return max_width, total_height


def draw_text_box_with_background(
    image: Image.Image,
    text_lines: list[str],
    font_size: int,
    y_position: int,
    padding: int = 18,
    opacity: float = 0.7,
    line_spacing: int = 10,
    bottom_padding: int = None,
    full_width: bool = False,
    colored_sections: bool = False,
    extend_to_bottom: bool = False
) -> Image.Image:
    img_width, img_height = image.size
    
    overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)
    
    font = get_cute_font(font_size)
    
    text_width, text_height = calculate_multiline_text_dimensions(draw, text_lines, font, line_spacing)
    
    if bottom_padding is None:
        bottom_padding = padding
    
    if full_width:
        box_width = img_width
        box_x = 0
    else:
        box_width = text_width + (padding * 2)
        box_x = (img_width - box_width) // 2
    
    box_y = y_position
    
    if extend_to_bottom:
        box_height = img_height - box_y
    else:
        box_height = text_height + padding + bottom_padding
    
    white_with_opacity = (255, 255, 255, int(255 * opacity))
    draw.rectangle(
        [(box_x, box_y), (box_x + box_width, box_y + box_height)],
        fill=white_with_opacity
    )
    
    current_y = box_y + padding
    current_section = None
    
    for line in text_lines:
        line_width, line_height = calculate_text_dimensions(draw, line, font)
        text_x = (img_width - line_width) // 2
        
        if colored_sections:
            if line.startswith("FOR:"):
                current_section = "FOR"
                text_color = (0, 128, 0, 255)
            elif line.startswith("AGAINST:"):
                current_section = "AGAINST"
                text_color = (255, 0, 0, 255)
            elif current_section == "FOR":
                text_color = (0, 128, 0, 255)
            elif current_section == "AGAINST":
                text_color = (255, 0, 0, 255)
            else:
                text_color = (0, 0, 0, 255)
        else:
            text_color = (0, 0, 0, 255)
        
        draw.text((text_x, current_y), line, fill=text_color, font=font)
        current_y += line_height + line_spacing
    
    return Image.alpha_composite(image, overlay)


def create_voter_card(
    source_image_path: Path,
    output_path: Path,
    name: str,
    positions: PoliticalPositions
) -> Path:
    original_image = load_image(source_image_path)
    image = create_white_background_with_shrunk_image(original_image, shrink_factor=0.75)
    img_width, img_height = image.size
    
    image = draw_text_box_with_background(
        image,
        text_lines=[name],
        font_size=130,
        y_position=int(img_height * 0.02),
        padding=60,
        opacity=0.7
    )
    
    position_lines = format_positions_text(name, positions)
    
    font_size = 58
    
    bottom_y_position = int(img_height * 0.66) - 20 + 5
    
    image = draw_text_box_with_background(
        image,
        text_lines=position_lines,
        font_size=font_size,
        y_position=bottom_y_position,
        padding=15,
        opacity=0.7,
        line_spacing=15,
        bottom_padding=40,
        full_width=True,
        colored_sections=True,
        extend_to_bottom=True
    )
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    rgb_image = image.convert('RGB')
    rgb_image.save(output_path, 'PNG')
    
    return output_path
