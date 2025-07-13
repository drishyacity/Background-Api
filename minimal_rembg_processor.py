import os
import logging
from PIL import Image
import tempfile
import io

logger = logging.getLogger(__name__)

class MinimalBackgroundRemover:
    """Minimal background remover using rembg with fallback"""
    
    def __init__(self):
        """Initialize the background remover"""
        self.rembg = None
        logger.info("MinimalBackgroundRemover initialized")
    
    def _get_rembg(self):
        """Lazy load rembg"""
        if self.rembg is None:
            try:
                import rembg
                self.rembg = rembg
                logger.info("Rembg loaded successfully")
            except Exception as e:
                logger.error(f"Failed to load rembg: {e}")
                raise e
        return self.rembg
    
    def remove_background(self, input_path, output_path, background_type='transparent', 
                         background_color=None, background_image_path=None):
        """
        Remove background from image using rembg
        """
        try:
            # Load and process the input image
            logger.info(f"Loading input image: {input_path}")
            with open(input_path, 'rb') as input_file:
                input_data = input_file.read()
            
            # Get rembg and remove background - using simple approach
            rembg = self._get_rembg()
            logger.info("Removing background with rembg...")
            
            # Use the simple remove function without session
            output_data = rembg.remove(input_data)
            
            # Convert to PIL Image
            subject_image = Image.open(io.BytesIO(output_data)).convert('RGBA')
            logger.info(f"Background removed. Image size: {subject_image.size}")
            
            # Apply background based on type
            if background_type == 'transparent':
                result_image = subject_image
                logger.info("Using transparent background")
                
            elif background_type == 'solid':
                result_image = self._apply_solid_background(subject_image, background_color)
                logger.info(f"Applied solid background: {background_color}")
                
            elif background_type == 'image':
                result_image = self._apply_image_background(subject_image, background_image_path)
                logger.info("Applied image background")
            
            # Save result
            result_image.save(output_path, 'PNG')
            logger.info(f"Result saved to: {output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error removing background: {str(e)}")
            return False
    
    def _apply_solid_background(self, subject_image, hex_color):
        """Apply solid color background"""
        try:
            # Convert hex to RGB
            hex_color = hex_color.lstrip('#')
            rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            
            # Create background
            background = Image.new('RGBA', subject_image.size, rgb_color + (255,))
            
            # Composite images
            result = Image.alpha_composite(background, subject_image)
            return result.convert('RGB')
        except Exception as e:
            logger.error(f"Error applying solid background: {e}")
            return subject_image.convert('RGB')
    
    def _apply_image_background(self, subject_image, bg_image_path):
        """Apply image background"""
        try:
            # Load background image
            bg_image = Image.open(bg_image_path).convert('RGBA')
            
            # Resize background to match subject
            bg_image = bg_image.resize(subject_image.size, Image.Resampling.LANCZOS)
            
            # Composite images
            result = Image.alpha_composite(bg_image, subject_image)
            return result.convert('RGB')
        except Exception as e:
            logger.error(f"Error applying image background: {e}")
            return subject_image.convert('RGB')